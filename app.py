import openai
import pandas as pd
from openai.embeddings_utils import get_embedding,cosine_similarity
import openai
import pandas as pd
from openai.embeddings_utils import get_embedding,cosine_similarity

from flask import Flask, request,make_response,jsonify
from chatbot import makeRequest
app = Flask(__name__)

api_key ="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"
openai.api_key = api_key

def makeRequest(input_string):
    product_data = [
            {
            "tourId": 19,
            "title": "Khám phá Địa đạo Củ Chi Chuyến đi nửa ngày",
            "city": "Hồ Chí Minh",
            "priceOnePerson": 5264000.0,
            "categoryName": "Nghệ thuật và văn hóa",
            "avgRating": 4.0
        },
        {
            "tourId": 20,
            "title": "Bí Mật Đằng Sau Món Cà Phê Trứng Trứ Danh Của Việt Nam",
            "city": "Hồ Chí Minh",
            "priceOnePerson": 360000.0,
            "categoryName": "Giải trí",
            "avgRating": 5.0
        },
        {
            "tourId": 31,
            "title": "Tour khám phá Sài Gòn với những bức ảnh tóm tắt tuyệt vời",
            "city": "Hồ Chí Minh",
            "priceOnePerson": 850000.0,
            "categoryName": "Giải trí",
            "avgRating": 3.5
        },
        {
            "tourId": 42,
            "title": "Retreat nửa ngày giữa thiên nhiên",
            "city": "Hội An",
            "priceOnePerson": 570000.0,
            "categoryName": "Thể thao",
            "avgRating": 4.0
        },
        {
            "tourId": 36,
            "title": "Khám phá cuộc sống nông thôn và tất cả về cà phê tại Elon Farm",
            "city": "Đà Lạt",
            "priceOnePerson": 1500000.0,
            "categoryName": "Thức ăn và đồ uống",
            "avgRating": 4.0
        },
        {
            "tourId": 40,
            "title": "Bài học lướt sóng nhanh một giờ và hai giờ cho thuê ván lướt sóng",
            "city": "Đà Nẵng",
            "priceOnePerson": 450000.0,
            "categoryName": "Thể thao",
            "avgRating": 5.0
        },
        {
            "tourId": 10,
            "title": "Những viên ngọc ẩn giấu của Hội An xưa",
            "city": "Hội An",
            "priceOnePerson": 950000.0,
            "categoryName": "Nghệ thuật và văn hóa",
            "avgRating": 3.5
        },
        {
            "tourId": 11,
            "title": "Khu bảo tồn Mỹ Sơn với hướng dẫn nội bộ",
            "city": "Hội An",
            "priceOnePerson": 950000.0,
            "categoryName": "Nghệ thuật và văn hóa",
            "avgRating": 4.5
        },
        {
            "tourId": 12,
            "title": "Bình minh trên thung lũng sương mù, Ăn bánh căn",
            "city": "Hội An",
            "priceOnePerson": 750000.0,
            "categoryName": "Nghệ thuật và văn hóa",
            "avgRating": 3.5
        },
        {
            "tourId": 13,
            "title": "Lớp học đèn lồng truyền thống ở Khu phố cổ",
            "city": "Hội An",
            "priceOnePerson": 190000.0,
            "categoryName": "Nghệ thuật và văn hóa",
            "avgRating": 4.5
        },
        {
            "tourId": 28,
            "title": "Ninh Bình cả ngày - chuyến đi bằng thuyền Tràng An - Núi Rồng",
            "city": "Hà Nội",
            "priceOnePerson": 1200000.0,
            "categoryName": "Giải trí",
            "avgRating": 4.5
        },
        {
            "tourId": 14,
            "title": "Ăn như người dân địa phương, với một người dân địa phương ở Huế",
            "city": "Huế",
            "priceOnePerson": 500000.0,
            "categoryName": "Nghệ thuật và văn hóa",
            "avgRating": 5.0
        },
        {
            "tourId": 15,
            "title": "Tour đi bộ Cố đô Huế",
            "city": "Huế",
            "priceOnePerson": 700000.0,
            "categoryName": "Nghệ thuật và văn hóa",
            "avgRating": 5.0
        },
        {   
            "tourId": 17,
            "title": "Nấu ăn tại nhà với gia đình Hội An của tôi",
            "city": "Hội An",
            "priceOnePerson": 879000.0,
            "categoryName": "Nghệ thuật và văn hóa",
            "avgRating": 4.0
        },
        {
            "tourId": 18,
            "title": "Ẩm thực đường phố Hà Nội theo nhóm nhỏ với một tín đồ ẩm thực",
            "city": "Hà Nội",
            "priceOnePerson": 500000.0,
            "categoryName": "Nghệ thuật và văn hóa",
            "avgRating": 4.5
        },
        {
            "tourId": 20,
            "title": "Bí Mật Đằng Sau Món Cà Phê Trứng Trứ Danh Của Việt Nam",
            "city": "Hồ Chí Minh",
            "priceOnePerson": 360000.0,
            "categoryName": "Giải trí",
            "avgRating": 5.0
        }
    ]

    product_data_df = pd.DataFrame(product_data)
    product_data_df

    product_data_df['combined'] = product_data_df.apply(lambda row: f"{row['title']}, {row['city']}, {row['priceOnePerson']}", axis=1)
    product_data_df

    product_data_df['text_embedding'] = product_data_df.combined.apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
    product_data_df

    customer_order_data = [
        {
            "tourId": 42,
            "title": "Retreat nửa ngày giữa thiên nhiên",
            "city": "Hội An",
            "priceOnePerson": 570000.0,
            "categoryName": "Thể thao",
            "avgRating": 4.0
        },
        {
            "tourId": 36,
            "title": "Khám phá cuộc sống nông thôn và tất cả về cà phê tại Elon Farm",
            "city": "Đà Lạt",
            "priceOnePerson": 1500000.0,
            "categoryName": "Thức ăn và đồ uống",
            "avgRating": 4.0
        },
        {
            "tourId": 14,
            "title": "Ăn như người dân địa phương, với một người dân địa phương ở Huế",
            "city": "Huế",
            "priceOnePerson": 500000.0,
            "categoryName": "Nghệ thuật và văn hóa",
            "avgRating": 5.0
        },
        {
            "tourId": 20,
            "title": "Bí Mật Đằng Sau Món Cà Phê Trứng Trứ Danh Của Việt Nam",
            "city": "Hồ Chí Minh",
            "priceOnePerson": 360000.0,
            "categoryName": "Giải trí",
            "avgRating": 5.0
        }
    ]

    customer_order_df = pd.DataFrame(customer_order_data)
    customer_order_df

    customer_order_df['combined'] = customer_order_df.apply(lambda row: f"{row['title']}, {row['city']}, {row['priceOnePerson']}", axis=1)
    customer_order_df

    customer_order_df['text_embedding'] = customer_order_df.combined.apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
    customer_order_df

    customer_input = input_string

    response = openai.Embedding.create(
        input=customer_input,
        model="text-embedding-ada-002"
    )
    embeddings_customer_question = response['data'][0]['embedding']

    customer_order_df['search_purchase_history'] = customer_order_df.text_embedding.apply(lambda x: cosine_similarity(x, embeddings_customer_question))
    customer_order_df = customer_order_df.sort_values('search_purchase_history', ascending=False)
    customer_order_df

    top_3_purchases_df = customer_order_df.head(2)
    top_3_purchases_df

    product_data_df['search_products'] = product_data_df.text_embedding.apply(lambda x: cosine_similarity(x, embeddings_customer_question))
    product_data_df = product_data_df.sort_values('search_products', ascending=False)
    product_data_df

    top_3_purchases_df = customer_order_df.head(2)
    top_3_purchases_df

    top_3_products_df = product_data_df.head(4)
    top_3_products_df

    message_objects = []
    message_objects.append({"role":"system", "content":"Bạn là một chatbot giúp khách hàng giải đáp các thắc mắc liên quan đến du lịch và giúp họ đưa ra các đề xuất du lịch"})


    # Append the customer messagae
    message_objects.append({"role":"user", "content": customer_input})

    # Create previously purchased input
    prev_purchases = ". ".join([f"{row['combined']}" for index, row in top_3_purchases_df.iterrows()])
    prev_purchases

    # Create list of 3 products to recommend
    products_list = []

    for index, row in top_3_products_df.iterrows():
        brand_dict = {'role': "assistant", "content": f"{row['combined']}"}
        products_list.append(brand_dict)
    products_list

    # Append found products  
    message_objects.append({"role": "assistant", "content": f"Tôi tìm thấy 3 chuyến đi này tôi muốn giới thiệu"})
    message_objects.extend(products_list)
    message_objects.append({"role": "assistant", "content":"Đây là đề xuất tóm tắt của tôi về các chuyến du lịch và lý do tại sao nó phù hợp với bạn:"})
    message_objects

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message_objects
    )
    return completion.choices[0].message['content']

@app.route('/api/v1/chatgpt', methods=['POST'])
def create_todo():
   data = request.get_json()
   result = makeRequest(data['message'])
   return make_response(jsonify({"chatgpt": result}), 200)

if __name__ == '__main__':
    app.run()
