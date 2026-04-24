from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn (document_id, source_type, author, category, content, timestamp). 
    TODO: Khai báo các trường với kiểu dữ liệu str ở dưới.
    """
    # Khai báo các trường ở đây...
    document_id: str
    source_type: str
    content: str
    
    # Sử dụng Optional (có thể có hoặc không) và gán mặc định là None vì 
    # trong thực tế một số file như vid2_missing_tags.json bị thiếu trường creator_name
    author: Optional[str] = None
    category: Optional[str] = None
    timestamp: Optional[str] = None
    pass
