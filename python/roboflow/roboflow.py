from libs.scrape import ScrapeFlicker
import os
from dotenv import load_dotenv
from libs.secretmanager import SecretManager

if __name__ == "__main__":




    load_dotenv()

    key = os.getenv("FLICKR_API_KEY")
    secret = os.getenv("FLICKR_API_SECRET")
    google_service_account = os.getenv("GOOGLE_SERVICE_ACCOUNT")

    urls = ScrapeFlicker(api_key=key, api_secret= secret,search="surfing").get_urls()

    secret_manager = SecretManager(project_id='neo4j-cs-team-201901', service_account_info=google_service_account)

    print(secret_manager)






