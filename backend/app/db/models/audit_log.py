from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.sql import func

from app.core.database import Base


class AuditLog(Base):
    """Audit log model - track all important actions"""
    __tablename__ = "audit_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Actor
    actor_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    actor_type = Column(String, nullable=False)  # user, system, api, etc.
    actor_name = Column(String, nullable=True)
    
    # Action
    action = Column(String, nullable=False, index=True)  # create_invoice, approve_tranche, etc.
    resource_type = Column(String, nullable=False, index=True)  # invoice, tranche, user, etc.
    resource_id = Column(Integer, nullable=True, index=True)
    
    # Organization context
    org_id = Column(Integer, ForeignKey("organizations.id"), nullable=True, index=True)
    
    # Details
    details_json = Column(Text, nullable=True)  # JSON with additional context
    
    # Request metadata
    ip_address = Column(String, nullable=True)
    user_agent = Column(String, nullable=True)
    request_id = Column(String, nullable=True, index=True)
    
    # Status
    status = Column(String, nullable=False)  # success, failure, pending
    error_message = Column(Text, nullable=True)
    
    # Timestamp
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    
    def __repr__(self):
        return f"<AuditLog {self.action} by {self.actor_name}>"
