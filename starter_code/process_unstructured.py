import re
from datetime import datetime

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================

def _safe_parse_timestamp(raw_value: str) -> datetime:
    """Parse timestamp string sang datetime, trả về datetime.min nếu lỗi."""
    if not raw_value:
        return datetime.min

    # Thử các format phổ biến
    formats = [
        "%Y-%m-%dT%H:%M:%SZ",   # ISO 8601 với Z
        "%Y-%m-%dT%H:%M:%S",    # ISO 8601 không Z
        "%Y-%m-%d %H:%M:%S",    # Standard datetime
        "%Y-%m-%d",              # Date only
        "%Y",                    # Year only
    ]
    for fmt in formats:
        try:
            return datetime.strptime(raw_value, fmt)
        except ValueError:
            continue

    return datetime.min


def process_pdf_data(raw_json: dict) -> dict:
    """Chuyển đổi dữ liệu PDF thô (camelCase) sang UnifiedDocument schema."""
    # Bước 1: Làm sạch nhiễu (Header/Footer) khỏi văn bản
    raw_text = raw_json.get("extractedText", "")
    cleaned_content = re.sub(r'HEADER_PAGE_\d+', '', raw_text)
    cleaned_content = re.sub(r'FOOTER_PAGE_\d+', '', cleaned_content)
    cleaned_content = cleaned_content.strip()

    # Bước 2: Map dữ liệu thô sang định dạng chuẩn của UnifiedDocument
    return {
        "document_id": raw_json.get("docId", ""),
        "source_type": "PDF",
        "author": raw_json.get("authorName", "Unknown").strip(),
        "category": raw_json.get("docCategory", ""),
        "content": cleaned_content,
        "timestamp": _safe_parse_timestamp(raw_json.get("createdAt", "")),
    }

def process_video_data(raw_json: dict) -> dict:
    """Chuyển đổi dữ liệu Video thô (snake_case) sang UnifiedDocument schema."""
    return {
        "document_id": raw_json.get("video_id", ""),
        "source_type": "Video",
        "author": raw_json.get("creator_name", "Unknown"),
        "category": raw_json.get("category", ""),
        "content": raw_json.get("transcript", ""),
        "timestamp": _safe_parse_timestamp(raw_json.get("published_timestamp", "")),
    }
