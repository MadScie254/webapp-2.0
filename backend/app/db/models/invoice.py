from sqlalchemy import Column, Integer, String, Numeric, DateTime, Text, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from app.core.database import Base


class InvoiceStatus(str, enum.Enum):
    """Invoice status enum"""
    DRAFT = "draft"
    ISSUED = "issued"
    PAYMENT_PENDING = "payment_pending"
    PARTIALLY_PAID = "partially_paid"
    PAID = "paid"
    OVERDUE = "overdue"
    CANCELLED = "cancelled"


class Invoice(Base):
    """Invoice model"""
    __tablename__ = "invoices"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Organization & Customer
    org_id = Column(Integer, ForeignKey("organizations.id"), nullable=False, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False, index=True)
    creator_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Invoice details
    invoice_number = Column(String, unique=True, nullable=False, index=True)
    
    # Financial
    amount = Column(Numeric(15, 2), nullable=False)
    currency = Column(String, default="USD")
    tax_amount = Column(Numeric(15, 2), default=0)
    total_amount = Column(Numeric(15, 2), nullable=False)
    amount_paid = Column(Numeric(15, 2), default=0)
    
    # Dates
    issued_date = Column(DateTime(timezone=True), nullable=False)
    due_date = Column(DateTime(timezone=True), nullable=False)
    payment_date = Column(DateTime(timezone=True), nullable=True)
    
    # Status
    status = Column(SQLEnum(InvoiceStatus), default=InvoiceStatus.DRAFT, nullable=False)
    
    # Description & Notes
    description = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    
    # OCR & Metadata
    ocr_extracted = Column(Boolean, default=False)
    ocr_confidence = Column(Numeric(5, 2), nullable=True)  # 0-100
    metadata_json = Column(Text, nullable=True)  # Additional metadata
    
    # File attachments
    file_url = Column(String, nullable=True)  # MinIO URL
    file_hash = Column(String, nullable=True)  # SHA256 for verification
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    organization = relationship("Organization")
    customer = relationship("Customer")
    creator = relationship("User")
    # tranches = relationship("Tranche", back_populates="invoice")
    # attestations = relationship("Attestation", back_populates="invoice")
    
    def __repr__(self):
        return f"<Invoice {self.invoice_number} - {self.total_amount} {self.currency}>"


from sqlalchemy import Boolean
