import os
import json
from modules.banners import banners
from modules.logging import log_error, log_info
from modules.args_parser import args_parser

OUTPUT_DIR = "DEVICE"

def main():
    args = args_parser()

    brand = args.brand.strip().upper()
    model = args.model.strip().upper()
    system_id = args.system_id.strip()
    security_level = args.security_level.strip()

    brand_dir = os.path.join(OUTPUT_DIR, brand)
    os.makedirs(brand_dir, exist_ok=True)

    model_filename = f"{model.replace('/', '_').replace(':', '_')}.json"
    output_path = os.path.join(brand_dir, model_filename)

    json_data = {
        "brand": brand,
        "model": model,
        "system_id": system_id,
        "security_level": security_level
    }

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4)
        log_info(f"Device entry created: {output_path}")
    except Exception as e:
        log_error(f"Failed to create device entry: {e}")
    
if __name__ == "__main__":
    banners()
    main()