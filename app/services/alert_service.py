from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.alert import Alert
from app.models.opportunity import Opportunity
from app.schemas.alert import AlertCreate, AlertUpdate

class AlertService:
    @staticmethod
    def create_alert(db: Session, alert_in: AlertCreate) -> Alert:
        db_alert = Alert(**alert_in.model_dump())
        db.add(db_alert)
        db.commit()
        db.refresh(db_alert)
        return db_alert

    @staticmethod
    def check_and_trigger_critical_alert(db: Session, opportunity: Opportunity):
        """
        Triggers a critical alert if (Impact + Urgency) >= 15.
        """
        score = (opportunity.impact_score or 0) + (opportunity.urgency_score or 0)
        
        if score >= 15:
            alert_in = AlertCreate(
                opportunity_id=opportunity.id,
                title="Critical Opportunity Detected!",
                message=f"New high-score opportunity ({score}/20) in {opportunity.primary_domain}.",
                severity="Critical"
            )
            AlertService.create_alert(db, alert_in)

    @staticmethod
    def get_alerts(db: Session, skip: int = 0, limit: int = 100) -> List[Alert]:
        return db.query(Alert).offset(skip).limit(limit).all()

    @staticmethod
    def mark_as_read(db: Session, alert_id: str) -> Optional[Alert]:
        db_alert = db.query(Alert).filter(Alert.id == alert_id).first()
        if db_alert:
            db_alert.is_read = True
            db.commit()
            db.refresh(db_alert)
        return db_alert

    @staticmethod
    def delete_alert(db: Session, alert_id: str) -> bool:
        db_alert = db.query(Alert).filter(Alert.id == alert_id).first()
        if db_alert:
            db.delete(db_alert)
            db.commit()
            return True
        return False
