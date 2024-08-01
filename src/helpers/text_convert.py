from pyodbc import Row


def convert_message(source_text: Row) -> str:
    article = source_text[1]
    name = source_text[2]
    link = f'https://www.wildberries.ru/catalog/{source_text[6]}/detail.aspx'
    rating = source_text[3]
    review_text = source_text[4]
    review_datetime = source_text[5].strftime("%d.%m.%Y")
    
    message = f"Артикул: {article}\n"\
        f"Наименование: {name}\n"\
        f"Ссылка на товар: {link}\n"\
        f"Оценка: {rating}\n"\
        f"Текст отзыва: {review_text}\n"\
        f"Дата отзыва: {review_datetime}"
        
    return message