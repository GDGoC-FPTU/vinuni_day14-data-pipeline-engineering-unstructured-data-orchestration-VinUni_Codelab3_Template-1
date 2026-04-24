# ==========================================
# ROLE 3: OBSERVABILITY & QA ENGINEER
# ==========================================

def run_semantic_checks(doc_dict: dict) -> bool:
    # 1. Kiểm tra các trường bắt buộc (Missing Core Fields Check)
    # Dựa vào yêu cầu thiết kế Schema, các trường quan trọng không được để trống
    required_fields = ["document_id", "source_type", "content"]
    for field in required_fields:
        if not doc_dict.get(field):
            return False

    content = str(doc_dict.get("content", ""))
    
    # 2. Kiểm tra độ dài: Nếu content trống hoặc quá ngắn sau khi xóa khoảng trắng
    if not content.strip() or len(content.strip()) < 10:
        return False
    
    # 3. Kiểm tra từ khóa lỗi (Toxic Keywords Check) - mở rộng danh sách lỗi OCR và hệ thống
    toxic_keywords = [
        "Null pointer exception", 
        "OCR Error", 
        "Traceback",
        "Internal Server Error",
        "404 Not Found",
        "Failed to extract text",
        "Unhandled exception",
        "undefined",
        "NaN"
    ]
    
    # Chuẩn hóa về chữ thường để tránh lọt lỗi do in hoa/in thường
    content_lower = content.lower()
    for keyword in toxic_keywords:
        if keyword.lower() in content_lower:
            return False

    # 4. Kiểm tra dữ liệu rác (Garbage Content Check)
    # Loại bỏ nếu văn bản chứa quá nhiều ký tự đặc biệt (tỷ lệ chữ/số < 40%)
    alnum_count = sum(c.isalnum() for c in content)
    if len(content) > 0 and (alnum_count / len(content)) < 0.4:
        return False
            
    return True
