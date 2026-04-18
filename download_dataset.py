# # # # Script to download dataset
# # # from icrawler.builtin import GoogleImageCrawler
# # # import os

# # # # All Indian cattle and buffalo breeds
# # # breeds = [
# # #     "Gir cow India",
# # #     "Sahiwal cow India",
# # #     "Ongole cow India",
# # #     "Kankrej cow India",
# # #     "Tharparkar cow India",
# # #     "Murrah buffalo India",
# # #     "Nili-Ravi buffalo India",
# # #     "Surti buffalo India",
# # #     "Jaffarabadi buffalo India"
# # # ]

# # # print("🐄 Starting dataset download...")
# # # print(f"Total breeds: {len(breeds)}")
# # # print("-" * 40)

# # # for breed in breeds:
# # #     # Create clean folder name
# # #     folder_name = breed.replace(" ", "_").replace("-", "_")
# # #     save_path = f"dataset/train/{folder_name}"
# # #     os.makedirs(save_path, exist_ok=True)

# # #     print(f"📥 Downloading: {breed}...")
# # #     try:
# # #         crawler = GoogleImageCrawler(
# # #             storage={"root_dir": save_path},
# # #             log_level=50  # Suppresses crawler logs
# # #         )
# # #         crawler.crawl(keyword=breed, max_num=80)
        
# # #         # Count downloaded images
# # #         count = len(os.listdir(save_path))
# # #         print(f"   ✅ {count} images saved → {save_path}")
# # #     except Exception as e:
# # #         print(f"   ❌ Failed: {e}")

# # # print("-" * 40)
# # # print("✅ Dataset download complete!")
# # # print(f"📁 Check folder: dataset/train/")

# # from icrawler.builtin import BingImageCrawler
# # import os

# # breeds = [
# #     "Gir cow India",
# #     "Sahiwal cow India",
# #     "Ongole cow India",
# #     "Kankrej cow India",
# #     "Tharparkar cow India",
# #     "Murrah buffalo India",
# #     "Nili-Ravi buffalo India",
# #     "Surti buffalo India",
# #     "Jaffarabadi buffalo India"
# # ]

# # print("🐄 Starting dataset download using Bing...")
# # print(f"Total breeds: {len(breeds)}")
# # print("-" * 40)

# # for breed in breeds:
# #     folder_name = breed.replace(" ", "_").replace("-", "_")
# #     save_path = f"dataset/train/{folder_name}"
# #     os.makedirs(save_path, exist_ok=True)

# #     print(f"📥 Downloading: {breed}...")
# #     try:
# #         crawler = BingImageCrawler(
# #             storage={"root_dir": save_path},
# #             feeder_threads=1,
# #             parser_threads=1,
# #             downloader_threads=4
# #         )
# #         crawler.crawl(keyword=breed, max_num=80)

# #         count = len(os.listdir(save_path))
# #         print(f"   ✅ {count} images saved → {save_path}")
# #     except Exception as e:
# #         print(f"   ❌ Failed: {e}")

# # print("-" * 40)
# # print("✅ All done!")

# from icrawler.builtin import BingImageCrawler
# import os

# # Download "Other" class images to reject non-animal images
# other_keywords = [
#     "nature landscape India",
#     "Indian temple",
#     "Indian village",
#     "Indian farmer",
#     "forest trees India"
# ]

# save_path = "dataset/train/Other"
# os.makedirs(save_path, exist_ok=True)

# for keyword in other_keywords:
#     print(f"📥 Downloading: {keyword}...")
#     crawler = BingImageCrawler(
#         storage={"root_dir": save_path},
#         feeder_threads=1,
#         parser_threads=1,
#         downloader_threads=4
#     )
#     crawler.crawl(keyword=keyword, max_num=20)

# count = len(os.listdir(save_path))
# print(f"✅ {count} Other images downloaded!")
# print("✅ Done! Now run: python train_model.py")
from icrawler.builtin import BingImageCrawler
import os

other_keywords = [
    "nature landscape India",
    "Indian temple",
    "Indian village",
    "Indian farmer",
    "forest trees India",
    "motivational quote wallpaper",
    "text poster wallpaper",
    "Indian food",
    "Indian festival",
    "Indian street",
    "mountain landscape",
    "ocean beach",
    "city buildings",
    "cartoon illustration",
    "abstract art"
]

save_path = "dataset/train/Other"
os.makedirs(save_path, exist_ok=True)

for keyword in other_keywords:
    print(f"📥 Downloading: {keyword}...")
    crawler = BingImageCrawler(
        storage={"root_dir": save_path},
        feeder_threads=1,
        parser_threads=1,
        downloader_threads=4
    )
    crawler.crawl(keyword=keyword, max_num=20)

count = len(os.listdir(save_path))
print(f"✅ {count} Other images downloaded!")