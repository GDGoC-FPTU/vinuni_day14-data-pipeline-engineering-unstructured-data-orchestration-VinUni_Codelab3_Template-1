# ==========================================
# ROLE 3: OBSERVABILITY & QA ENGINEER
# ==========================================

def run_semantic_checks(doc_dict: dict) -> bool:
    content = doc_dict.get("content", "")
    
    # 1. Kiểm tra độ dài: Nếu content trống hoặc < 10 ký tự -> False
    if not isinstance(content, str):
        content = str(content)
    if len(content.strip()) < 10:
        return False
    
    # 2. Kiểm tra từ khóa lỗi
    toxic_keywords = ["Null pointer exception", "OCR Error", "Traceback"]
    lowered_content = content.lower()
    for keyword in toxic_keywords:
        if keyword.lower() in lowered_content:
            return False
            
    return True
