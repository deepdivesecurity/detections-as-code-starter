from sigma.processing.pipeline import ProcessingPipeline

def sentinel_pipeline():
    return ProcessingPipeline(
        name="sentinel-custom",
        category_to_table_mapping={
            "okta": "Okta_CL"
        },
    )