from main.d_vs_c import logger
from main.d_vs_c.pipelines.data_ingestion_pipeline import data_inges_pipeline



if __name__ == '__main__':
    try:
        logger.info ('>>>>>>>>>>>>>>>>  Stage Data Ingestion Process Started...')
        obj = data_inges_pipeline()
        obj.main()
        logger.info('>>>>>>>>>>>>>>>Data Ingestion Proess Completed........')
        logger.info('<<<<<<<<<<<<<<<<<<<<')
    except Exception as e:
        raise e
else:
    print('dd')