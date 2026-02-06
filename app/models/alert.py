from sqlalchemy import Column, String, Text, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
import uuid

from app.models.base import Base

class Alert(Base):
    __tablename__ = "alerts"
    
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    opportunity_id = Column(String, ForeignKey("signal_analysis_opportunity.id"), nullable=False)
    title = Column(String(200), nullable=False)
    message = Column(Text, nullable=False)
    severity = Column(String(20), nullable=False) # 'Low', 'Medium', 'High', 'Critical'
    is_read = Column(Boolean, default=False)
    
    # Relationships
    opportunity = relationship("Opportunity")
