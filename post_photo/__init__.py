from fastapi import APIRouter, UploadFile


photo_router = APIRouter(prefix='/photo', tags=['Фотографии к постам'])

from post_photo import post_photo_api
# # Добавить фото к публикации (пример)
# @photo_router.post('/upload-photo')
# async def upload_photo_api(post_id: int, photo_file: UploadFile):
#     # Сохранение фотографии в локальную папку
#     with open('media/image.jpg', 'wb') as new_photo:
#         front_file_read = await photo_file.read()
#         new_photo.write(front_file_read)
#
#     return {'message': 'фото добавлено'}






# Получить прямую ссылку на фото
@photo_router.get('/get-photo')
async def get_photo_url():
    pass
