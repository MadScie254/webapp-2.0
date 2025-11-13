from sqlalchemy import Column, Integer, String, Numeric, DateTime, Text, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from app.core.database import Base


class TrancheStatus(str, enum.Enum):
    """Tranche status enum"""
    OPEN = "open"
    FUNDING = "funding"
    FUNDED = "funded"
    ACTIVE = "active"
    REPAYING = "repaying"
    COMPLETED = "completed"
    DEFAULTED = "defaulted"
    CANCELLED = "cancelled"


class Tranche(Base):
    """Tranche model - invoice financing micro-shares"""
    __tablename__ = "tranches"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Invoice relationship
    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False, index=True)
    
    # Tranche details
    tranche_number = Column(String, unique=True, nullable=False, index=True)
    share_amount = Column(Numeric(15, 2), nullable=False)  # Size of this tranche
    price = Column(Numeric(15, 2), nullable=False)  # Purchase price (may include discount)
    
    # Funding
    pledged_amount = Column(Numeric(15, 2), default=0)
    funded_amount = Column(Numeric(15, 2), default=0)
    target_amount = Column(Numeric(15, 2), nullable=False)
    
    # Returns
    expected_return = Column(Numeric(15, 2), nullable=True)
    actual_return = Column(Numeric(15, 2), nullable=True)
    return_percentage = Column(Numeric(5, 2), nullable=True)  # Yield %
    
    # Risk
    risk_band = Column(String, nullable=True)  # A, B, C, D, etc.
    risk_score = Column(Numeric(5, 2), nullable=True)  # 0-100
    
    # Status
    status = Column(SQLEnum(TrancheStatus), default=TrancheStatus.OPEN, nullable=False)
    
    # Dates
    open_date = Column(DateTime(timezone=True), server_default=func.now())
    funding_deadline = Column(DateTime(timezone=True), nullable=True)
    funded_date = Column(DateTime(timezone=True), nullable=True)
    maturity_date = Column(DateTime(timezone=True), nullable=True)
    closed_date = Column(DateTime(timezone=True), nullable=True)
    
    # Terms
    terms = Column(Text, nullable=True)
    minimum_investment = Column(Numeric(15, 2), nullable=True)
    maximum_investment = Column(Numeric(15, 2), nullable=True)
    
    # Metadata
    metadata_json = Column(Text, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    invoice = relationship("Invoice")
    # pledges = relationship("Pledge", back_populates="tranche")
    
    def __repr__(self):
        return f"<Tranche {self.tranche_number} - {self.share_amount}>"
