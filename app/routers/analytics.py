from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Dict, Any, List

from app.dependencies import get_db, get_current_user
from app.schemas.analytics import DashboardResponse, MarketTrendResponse
from app.services.analytics_service import AnalyticsService
from app.models.user import User

router = APIRouter()

@router.get("/dashboard", response_model=DashboardResponse)
def get_dashboard_summary(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Returns the comprehensive dashboard dataset including market trends.
    """
    trends = AnalyticsService.get_market_trends(db)
    tech_radar = AnalyticsService.get_tech_radar(db)
    entities = AnalyticsService.get_entities(db)
    funnel = AnalyticsService.get_funnel(db)
    benchmarks = AnalyticsService.get_benchmarks(db)
    return {
        "status": "success",
        "trends": trends,
        "tech_radar": tech_radar,
        "entities": entities,
        "funnel": funnel,
        "benchmarks": benchmarks,
        "metrics": {
            "total_active_sectors": len(set(t.domain_name for t in trends)),
            "total_technologies_tracked": len(set(tr.tech_name for tr in tech_radar)),
            "total_entities_tracked": len(entities)
        }
    }

@router.post("/calculate-trends", status_code=status.HTTP_202_ACCEPTED)
def trigger_trend_calculation(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """
    Manually triggers the AI data aggregation for the dashboard.
    """
    AnalyticsService.calculate_daily_trends(db)
    AnalyticsService.calculate_tech_radar(db)
    AnalyticsService.calculate_entities(db)
    AnalyticsService.calculate_funnel(db)
    return {"message": "All dashboard calculations started successfully"}
