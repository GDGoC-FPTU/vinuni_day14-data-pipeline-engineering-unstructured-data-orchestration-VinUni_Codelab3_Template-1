import re

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================

def process_pdf_data(raw_json: dict) -> dict:
    # Bước 1: Làm sạch nhiễu (Header/Footer) khỏi văn bản
    raw_text = raw_json.get("extractedText", "")
    
    # Dùng re.sub để xóa 'HEADER_PAGE_X' và 'FOOTER_PAGE_X' (với X là các chữ số)
    # Thêm .strip() để loại bỏ khoảng trắng thừa ở đầu/cuối sau khi xóa
    cleaned_content = re.sub(r'(HEADER_PAGE_\d+|FOOTER_PAGE_\d+)', '', raw_text).strip()
    
    # Bước 2: Map dữ liệu thô sang định dạng chuẩn của UnifiedDocument
    # Lưu ý: Các key như 'pdf_id', 'author', 'category' là giả định. 
    # Hãy thay đổi chúng cho khớp với JSON đầu vào thực tế của file PDF.
    return {
        "document_id": str(raw_json.get("pdf_id", "unknown_id")),
        "source_type": "PDF",
        "author": str(raw_json.get("author", "unknown_author")),
        "category": str(raw_json.get("category", "unknown_category")),
        "content": cleaned_content,
        "timestamp": str(raw_json.get("timestamp", "1970-01-01T00:00:00Z"))
    }

def process_video_data(raw_json: dict) -> dict:
    # Map dữ liệu thô từ Video sang định dạng chuẩn
    # Sử dụng các key: video_id, creator_name, transcript, category, published_timestamp
    return {
        "document_id": str(raw_json.get("video_id", "unknown_id")),
        "source_type": "Video",
        "author": str(raw_json.get("creator_name", "unknown_author")),
        "category": str(raw_json.get("category", "unknown_category")),
        "content": str(raw_json.get("transcript", "")),
        "timestamp": str(raw_json.get("published_timestamp", "1970-01-01T00:00:00Z"))
    }