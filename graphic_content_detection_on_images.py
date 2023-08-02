def categorize_images_based_on_safesearch(image_urls, api_key):
    graphic_censor_failed_pictures = {}
    graphic_content_verified_map = {}

    for x, y in enumerate(image_urls):
        safe_search, _ = analyze_image_url(y, api_key)

        if safe_search is None:
            continue

        if (
            safe_search["adult"] in ("LIKELY", "VERY_LIKELY")
            or safe_search["medical"] in ("LIKELY", "VERY_LIKELY")
            or safe_search["violence"] in ("LIKELY", "VERY_LIKELY")
        ):
            graphic_censor_failed_pictures["profilePic", x : y]
        else:
            graphic_content_verified_map["profilePic", x : y]

    return graphic_censor_failed_pictures, graphic_content_verified_map
