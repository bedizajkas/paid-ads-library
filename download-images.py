#!/usr/bin/env python3
"""
Download all images from the Killer Ads Library to your Downloads folder
"""

import requests
import os
from pathlib import Path
from datetime import datetime

# All your image URLs
URLS = [
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/73e77730-c937-4688-8e4f-950cb65289d0.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/50390896-ec3b-4c1d-aafa-e80ac8209a57.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/7aa981c5-b2ff-4d22-8244-01cab678206a.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/539302ce-049c-43fe-985e-05c1c8603aa3.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/8f677b11-bfe1-455b-863e-a3e4cb948411.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/28480647-dc5b-4664-8ee0-65a91d23e54c.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/1964f0c9-cfab-4ae1-b07c-9bea1b1cfd68.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/f47c154c-3c1f-474c-af71-71157208a344.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/25f8ddfb-b7a4-42b3-8ef9-1512f577dfd1.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/b0b5e456-fe86-4962-a0f5-7aa3559dfdce.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/2a201018-dcd0-4d37-90ab-3a7bf4652811.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/f0d7f90b-205c-4901-ba32-db7dd36da49f.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/94b1e1f9-06c0-48a4-b3c0-22bc2fb0dd42.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/fcab800f-f237-4f50-bb4b-304e6a3b16ef.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/fe63ab09-de11-4efc-9107-c37168f6aad9.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/4f184ce7-3136-407e-9db8-b0c34bf5b0a6.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/a3f39043-5fca-4b75-8511-b6180313a499.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/db8c0df8-ab23-4c4c-b5bb-1df2be007226.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/00c777e5-6dcf-4c3c-9d7d-754eaac83f1b.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/c2c53599-bfe7-41ea-bbac-f1a73fa0f95d.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/a69989e6-8d96-499e-a571-36bea9fdc917.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/5ca66eec-dd6f-4689-9a8a-30fc84cdb3d0.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/e253631c-c7db-4f42-971b-c6566d39b5bc.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/2f4d6dbe-1e3b-4005-9c9a-f97b0b67f460.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/64ab2672-d39b-4694-9ee0-5ab8e380e27a.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/c2024bfd-f077-4326-8d92-32df79f2ee9a.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/edb2854a-2a7f-4df1-bd03-c395c7fe203d.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/a04174dc-3b90-41b4-8f66-a71efb0883fc.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/e7a0588e-5804-4b73-843b-94b6c4e5474f.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/f7e57c13-26ad-4446-9a57-3f97125a5faf.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/12b10920-9765-4cd9-8378-9e6333655201.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/cdeadd31-c1f9-4cd5-ab95-ec36b7cce3b7.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/c65394ce-1e3b-4d28-ab1a-7f0743070408.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/becdadd6-2241-46eb-9bef-8c4024a44ecb.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/2c06842e-9326-4634-a35a-bb595a05845f.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/3a112416-554c-4ca3-870b-0185db483744.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/2610d699-dd97-43e8-8aed-f96ebfd00735.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/96db7cc8-0cee-4983-9273-d0668d7b74fd.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/45695095-f271-40f6-8828-c49cbb8a2d81.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/3036528f-39d2-403e-b63c-0b4845f735d6.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/903fae5d-befe-483a-9547-3e323d806428.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/c326ee2c-7bf9-47f9-a31e-0f31d61904ae.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/e71cff93-ae6f-4921-85a2-91152b593552.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/5ad8848d-c0bf-41f2-acc3-58b749f04083.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/e8c91562-9ec3-4371-b5db-68649a119bb8.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/c53d07fa-a76c-44ab-8611-60bc38cbfc06.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/a7ef1736-efb4-4ecf-8dc8-21b1906ab394.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/d692827c-57ab-4cb9-9959-476fa82045ee.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/cdf598e4-7126-404d-b338-bd195734eb36.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/b788d5ec-4a46-4a41-945e-0b8bbb3690e8.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/648dc14b-147d-4238-81e2-17cea4d8e09b.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/cdf294f0-0e03-4272-8f35-e1c0f668b927.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/d4d25a6d-dd8f-4517-9df5-b29b693c94d6.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/2a721e67-8028-43b7-8e4d-53f750d32881.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/0e4a0bf2-aecb-473e-a5e9-6aa79920c7c1.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/2f1fd413-a108-4037-bf2b-0895204163fe.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/824d5071-2c64-43f9-a954-b961fe085674.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/e1b5617d-f95f-43db-b830-b804736f8c3e.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/0d9a1aad-db9c-442b-a84f-c486a9d3f2b7.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/a23709c5-b0bf-4903-a9a0-81d558ef5f57.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/850c95e1-37ec-4fe8-9b8c-8699f34e7201.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/6456f220-3446-451e-877d-a0cd1eb41848.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/2fce825c-3c95-4e62-951c-6d2c18545bf8.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/02ae5370-a43a-4133-8e6b-1c9334504e02.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/e271b0a1-e405-4d5e-bcbb-61e5563cf7fa.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/deac8d18-f2e0-42e8-a45f-831782fd4a73.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/35105af4-fb12-43d7-953d-fcffc5c19ad5.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/c0370721-cb6c-4f38-b530-9d0f0f9c5ee4.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/62925df4-24c2-4faf-b968-fa4e43c41fca.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/332a2907-3a0b-47d3-a844-2e5726834769.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/cb68e8d2-219a-4650-8cd7-15427da3e573.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/550c3f38-7251-4150-9872-1c626d28a626.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/8fd21b6c-69eb-4626-a3dd-2a6d135d1a07.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/c30e6e4f-0a2b-48ae-8867-7e3dbbc0ed3a.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/367f6c2d-4f4e-45c8-928c-b81c163349cd.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/5341282e-3ac9-46a1-90d8-e0a608141cd9.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/8fbb6ce6-2710-44b1-bec2-2e364083e1c3.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/8da776a6-1a3b-435c-86e1-33a1f9fae3ce.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/05bb8404-713e-474a-bf23-c06ddf2b179a.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/16924737-ef85-4f05-adb7-dedecac57ab9.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/b9f22573-f9e2-4d0c-a319-f38d45e09e42.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/9108e924-43f6-4cb4-94b8-b0c87517be24.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/35043b08-cc0a-4f3f-b042-536cac0b3e60.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/12513bad-5bb9-494d-9065-0e49ec4b1652.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/f4c57958-9942-4b17-b035-c02d0947c9d8.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/3c52bd05-b209-44b9-af10-82d75ea2c93a.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/f3ae096a-6235-429e-904e-367d58c0ddb4.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/72476c68-2f40-4dc9-b52e-fa186bf38620.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/0e810f60-7684-4403-9935-b28ceebbafa0.png",
    "https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/37e96359-708b-4407-ad2e-7345924f6248.png"
]

def download_images():
    """Download all images to Downloads/paid-ads-images folder"""
    
    # Create output directory in Downloads
    downloads_dir = Path.home() / "Downloads"
    output_dir = downloads_dir / "paid-ads-images"
    output_dir.mkdir(exist_ok=True)
    
    print("🔥 Killer Paid Ads Library - Image Downloader")
    print("="*60)
    print(f"📥 Downloading {len(URLS)} images...")
    print(f"📁 Saving to: {output_dir}")
    print("="*60 + "\n")
    
    success = 0
    failed = 0
    failed_urls = []
    
    for i, url in enumerate(URLS, 1):
        try:
            # Create numbered filename (easier to work with)
            original_filename = url.split('/')[-1]
            numbered_filename = f"ad-{i:03d}.png"  # e.g., ad-001.png, ad-002.png
            filepath = output_dir / numbered_filename
            
            # Skip if already downloaded
            if filepath.exists():
                print(f"⏭️  [{i:2d}/{len(URLS)}] Already exists: {numbered_filename}")
                success += 1
                continue
            
            # Download the image
            print(f"⬇️  [{i:2d}/{len(URLS)}] Downloading: {numbered_filename}", end="", flush=True)
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            # Save to file
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            success += 1
            print(f" ✅")
            
        except Exception as e:
            failed += 1
            failed_urls.append((i, url, str(e)))
            print(f" ❌ Failed: {str(e)[:50]}")
    
    # Summary
    print("\n" + "="*60)
    print("📊 DOWNLOAD COMPLETE!")
    print("="*60)
    print(f"✅ Successfully downloaded: {success}/{len(URLS)} images")
    if failed > 0:
        print(f"❌ Failed: {failed}/{len(URLS)} images")
        print("\nFailed URLs:")
        for num, url, error in failed_urls:
            print(f"  {num}. {url.split('/')[-1][:40]}... - {error[:50]}")
    print(f"\n📁 Location: {output_dir}")
    print("="*60)
    
    # Open folder in Finder (Mac)
    if success > 0:
        print("\n💡 Opening folder in Finder...")
        os.system(f'open "{output_dir}"')

if __name__ == "__main__":
    try:
        download_images()
    except KeyboardInterrupt:
        print("\n\n⚠️  Download interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Error: {str(e)}")

