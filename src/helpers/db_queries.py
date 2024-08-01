def get_select_reviews_query() -> str:
    return "exec TGNotifyFeedback.getFeedbacksForNotify"
    
def get_update_review_query(review_id) -> str:
    return f"UPDATE wb.feedbacks SET telegramNotifyDate = getdate() WHERE id='{review_id}'"