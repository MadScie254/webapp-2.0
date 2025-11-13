from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Attestation(Base):
    """Attestation model - agent-verified invoice proof"""
    __tablename__ = "attestations"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Relationships
    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False, index=True)
    agent_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    
    # Attestation type
    attestation_type = Column(String, nullable=False)  # inspection, delivery, payment_proof, etc.
    
    # Media & Proof
    media_url = Column(String, nullable=True)  # Photo/video in MinIO
    file_hash = Column(String, nullable=False, index=True)  # SHA256 of file
    
    # Signature & Verification
    signature = Column(Text, nullable=False)  # JSON-LD signed attestation
    signature_algorithm = Column(String, default="RS256")
    public_key_id = Column(String, nullable=True)
    
    # IPFS (optional)
    ipfs_hash = Column(String, nullable=True, index=True)
    
    # Location & Context
    latitude = Column(String, nullable=True)
    longitude = Column(String, nullable=True)
    location_accuracy = Column(Integer, nullable=True)  # meters
    
    # Device metadata (privacy-safe)
    device_timestamp = Column(DateTime(timezone=True), nullable=True)
    device_metadata = Column(Text, nullable=True)  # JSON: OS, app version, etc.
    
    # Notes
    notes = Column(Text, nullable=True)
    metadata_json = Column(Text, nullable=True)
    
    # Verification status
    is_verified = Column(Boolean, default=False)
    verified_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    verified_at = Column(DateTime(timezone=True), nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    invoice = relationship("Invoice")
    agent = relationship("User", foreign_keys=[agent_id])
    verifier = relationship("User", foreign_keys=[verified_by])
    
    def __repr__(self):
        return f"<Attestation {self.id} for Invoice {self.invoice_id}>"


from sqlalchemy import Boolean
