from sqlalchemy import Column, Integer, String, Numeric, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class ScoreCache(Base):
    """Credit score cache model"""
    __tablename__ = "score_cache"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Entity being scored (organization or user)
    org_id = Column(Integer, ForeignKey("organizations.id"), nullable=True, index=True)
    entity_id = Column(Integer, nullable=False, index=True)  # Generic entity ID
    entity_type = Column(String, nullable=False)  # organization, user, customer, etc.
    
    # Score
    score = Column(Numeric(5, 2), nullable=False)  # 0-100
    score_band = Column(String, nullable=True)  # A, B, C, D, etc.
    confidence = Column(Numeric(5, 2), nullable=True)  # 0-100
    
    # Model metadata
    model_version = Column(String, nullable=False)
    model_type = Column(String, nullable=False)  # lightgbm, logistic_regression, etc.
    
    # Features used
    features_json = Column(Text, nullable=False)  # JSON of features used
    
    # SHAP explainability
    shap_values = Column(Text, nullable=True)  # JSON of SHAP values
    top_features = Column(Text, nullable=True)  # JSON of top contributing features
    
    # Validity
    valid_until = Column(DateTime(timezone=True), nullable=True)
    is_valid = Column(Boolean, default=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    organization = relationship("Organization")
    
    def __repr__(self):
        return f"<ScoreCache {self.entity_type}:{self.entity_id} = {self.score}>"


from sqlalchemy import Boolean
