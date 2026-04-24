from typing import Literal
from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Unified Schema for unstructured data (PDF and Video).
    Ensures consistent data format for downstream AI processing.
    """
    document_id: str = Field(..., description="Unique identifier for the document")
    source_type: Literal["PDF", "Video"] = Field(..., description="Type of data source")
    author: str = Field(..., description="Author or creator of the content")
    category: str = Field(..., description="Domain category")
    content: str = Field(..., min_length=1, description="Main text content or transcript")
    timestamp: str = Field(..., description="Creation or publication time (ISO format)")
