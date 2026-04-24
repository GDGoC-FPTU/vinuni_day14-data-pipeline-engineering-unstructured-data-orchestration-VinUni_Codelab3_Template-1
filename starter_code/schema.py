from datetime import datetime

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
    document_id: str = Field(..., description="Định danh duy nhất của tài liệu")
    source_type: str = Field(..., description="Loại nguồn dữ liệu (ví dụ: pdf, web, note)")
    author: str = Field(..., description="Tác giả hoặc người tạo nội dung")
    category: str = Field(..., description="Nhóm hoặc chủ đề để phân loại tài liệu")
    content: str = Field(..., description="Nội dung chính của tài liệu")
    timestamp: datetime = Field(..., description="Thời điểm tạo/cập nhật tài liệu (datetime)")
