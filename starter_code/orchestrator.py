import os
import json
import glob

# Import các thành phần
from schema import UnifiedDocument
from process_unstructured import process_pdf_data, process_video_data
from quality_check import run_semantic_checks

# ==========================================
# ROLE 4: DEVOPS & INTEGRATION SPECIALIST
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DATA_DIR = os.path.join(BASE_DIR, "..", "raw_data")
OUTPUT_FILE = os.path.join(BASE_DIR, "..", "processed_knowledge_base.json")

def run_pipeline():
    final_kb = []
    
    # Xử lý Group A (PDFs)
    pdf_files = glob.glob(os.path.join(RAW_DATA_DIR, "group_a_pdfs", "*.json"))
    for file_path in pdf_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
        
        # Bước 1: Gọi hàm xử lý PDF
        processed_doc = process_pdf_data(raw_data)
        
        # Bước 2: Kiểm tra chất lượng và giữ lại bản ghi hợp lệ
        if run_semantic_checks(processed_doc):
            final_kb.append(processed_doc)

    # Xử lý Group B (Videos)
    video_files = glob.glob(os.path.join(RAW_DATA_DIR, "group_b_videos", "*.json"))
    for file_path in video_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
        
        # Tương tự PDF: xử lý dữ liệu thô, chạy quality gate, rồi append nếu pass
        processed_doc = process_video_data(raw_data)
        if run_semantic_checks(processed_doc):
            final_kb.append(processed_doc)

    # Lưu kết quả
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_kb, f, indent=4)
        print(f"Pipeline finished! Saved {len(final_kb)} records.")

if __name__ == "__main__":
    run_pipeline()
