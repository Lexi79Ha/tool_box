import requests
import os
import logging

def fetch_and_save_block_data(block_number, folder):
    # Make the API request
    url = f"http://116.202.143.93:1317/cosmos/base/tendermint/v1beta1/blocks/5799128"
    response = requests.get(url)

    # Extract the height from the response (assuming it's available)
    height = response.json().get("block", {}).get("header", {}).get("height")

    # Construct the filename based on the height
    fetch_filename = os.path.join(folder, f"{height}.json")

    # Save the response content to the dynamically named file
    with open(fetch_filename, "wb") as f:
        f.write(response.content)

    return height, fetch_filename  # Return the filename for testing purposes

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(filename="log.txt", level=logging.INFO)
    logger = logging.getLogger()

    # Create a separate logger for errors
    error_logger = logging.getLogger("error_logger")
    error_logger.setLevel(logging.ERROR)
    error_handler = logging.FileHandler("error.txt")
    error_logger.addHandler(error_handler)

    try:
        folder_path = "C:/Users/lmhmo/indexer/blocks"
        _, saved_filename = fetch_and_save_block_data(1000000, folder_path)
        logger.info(f"Data saved to {saved_filename}")
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        error_logger.error(f"Error occurred: {str(e)}")


