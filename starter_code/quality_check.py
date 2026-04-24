# ==========================================
# ROLE 3: OBSERVABILITY & QA ENGINEER
# ==========================================

def run_semantic_checks(doc_dict: dict) -> bool:
    content = doc_dict.get("content", "")
    
    # 1. Kiểm tra độ dài: Nếu content trống hoặc < 10 ký tự -> False
    # TODO: Thực hiện kiểm tra độ dài ở đây
    if len(content) < 10:
        return False
    
    # 2. Kiểm tra từ khóa lỗi
    toxic_keywords = ["Null pointer exception", "OCR Error", "Traceback"]
    # TODO: Lặp qua các từ trong toxic_keywords, nếu từ đó xuất hiện trong content -> Trả về False
    for keyword in toxic_keywords:
        if keyword in content:
            return False
            
    return True
