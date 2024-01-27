from datetime import date

from src.email.send_email import send_email
from src.etls.bocm.scrapper import BOCMScrapper
from src.etls.common.etl import ETL
from src.initialize import initialize_app

if __name__ == "__main__":
    INIT_OBJECTS = initialize_app()
    etl_job = ETL(
        config_loader=INIT_OBJECTS.config_loader, vector_store=INIT_OBJECTS.vector_store
    )
    bocm_scrapper = BOCMScrapper()
    day = date.today()
    docs = bocm_scrapper.download_day(day)
    if docs:
        etl_job.run(docs)

    subject = "[BOCM] Daily ETL executed"
    content = f"""
    Daily ETL executed
    - Date: {day}
    - Documents loaded: {len(docs)} 
    - Database used: {INIT_OBJECTS.config_loader['vector_store']}
    """
    #send_email(INIT_OBJECTS.config_loader, subject, content)
