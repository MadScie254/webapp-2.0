from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from app.core.database import Base


class UserRole(str, enum.Enum):
    """User roles in the system"""
    ADMIN = "admin"
    AGENT = "agent"
    BORROWER = "borrower"
    INVESTOR = "investor"
    OPERATOR = "operator"


class User(Base):
    """User model"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_hash = Column(String, index=True)  # Hashed for privacy
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    role = Column(SQLEnum(UserRole), default=UserRole.BORROWER, nullable=False)
    
    # Organization relationship
    org_id = Column(Integer, nullable=True)  # Will add FK later
    
    # Status
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    
    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_login = Column(DateTime(timezone=True), nullable=True)
    
    # Profile metadata (JSON)
    profile_metadata = Column(Text, nullable=True)  # Store as JSON string
    
    # Relationships (will be defined after other models)
    # organization = relationship("Organization", back_populates="users")
    # invoices = relationship("Invoice", back_populates="creator")
    # attestations = relationship("Attestation", back_populates="agent")
    
    def __repr__(self):
        return f"<User {self.email} ({self.role})>"
