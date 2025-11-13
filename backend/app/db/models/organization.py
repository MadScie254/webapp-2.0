from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Organization(Base):
    """Organization model - represents MFIs, SACCOs, SMEs"""
    __tablename__ = "organizations"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    
    # Contact & Location
    country = Column(String, nullable=False)
    region = Column(String, nullable=True)
    address = Column(Text, nullable=True)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    
    # Admin user
    admin_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Organization type
    org_type = Column(String, nullable=True)  # MFI, SACCO, SME, etc.
    
    # Registration & compliance
    registration_number = Column(String, nullable=True, index=True)
    tax_id = Column(String, nullable=True)
    
    # Status
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    
    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Settings (JSON)
    settings = Column(Text, nullable=True)  # Store as JSON string
    
    # Relationships
    admin = relationship("User", foreign_keys=[admin_id])
    # users = relationship("User", back_populates="organization")
    # invoices = relationship("Invoice", back_populates="organization")
    # customers = relationship("Customer", back_populates="organization")
    
    def __repr__(self):
        return f"<Organization {self.name}>"


from sqlalchemy import Boolean
