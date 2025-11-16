#!/usr/bin/env python3
"""
Helper script to convert a list of URLs into JavaScript array format
Perfect for embedding into the HTML viewer!

Usage:
1. Create a file called 'urls.txt' with one URL per line
2. Run: python convert-urls.py
3. Copy the output and paste it into the HTML file's PERMANENT_URLS section
"""

def convert_urls_to_js_array(input_file='urls.txt', output_file='urls-formatted.txt'):
    """Convert plain text URLs to JavaScript array format"""
    
    try:
        with open(input_file, 'r') as f:
            urls = [line.strip() for line in f if line.strip() and line.strip().startswith('http')]
        
        if not urls:
            print("❌ No valid URLs found in", input_file)
            print("Make sure each URL is on its own line and starts with http:// or https://")
            return
        
        # Generate JavaScript array
        js_array = "const PERMANENT_URLS = [\n"
        for i, url in enumerate(urls):
            # Add comma for all except last item
            comma = "," if i < len(urls) - 1 else ""
            js_array += f'    "{url}"{comma}\n'
        js_array += "];"
        
        # Save to file
        with open(output_file, 'w') as f:
            f.write(js_array)
        
        print(f"✅ Success! Converted {len(urls)} URLs")
        print(f"📄 Output saved to: {output_file}")
        print("\n" + "="*60)
        print("📋 Copy everything below and paste into your HTML file:")
        print("="*60 + "\n")
        print(js_array)
        print("\n" + "="*60)
        print("\n💡 Next steps:")
        print("1. Open image-viewer.html in a code editor")
        print("2. Find the PERMANENT_URLS section (around line 220)")
        print("3. Replace the existing array with the output above")
        print("4. Save and share the HTML file!")
        
    except FileNotFoundError:
        print(f"❌ File '{input_file}' not found!")
        print("\nCreating example file...")
        with open(input_file, 'w') as f:
            f.write("https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/image1.png\n")
            f.write("https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/image2.png\n")
            f.write("https://userdata-f1db6c.stack.tryrelevance.com/conversation/files/image3.png\n")
        print(f"✅ Created example '{input_file}' file")
        print("📝 Replace the example URLs with your real URLs and run this script again!")

if __name__ == "__main__":
    import sys
    
    # Check if custom input file provided
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'urls.txt'
    
    print("🔄 Converting URLs to JavaScript array format...\n")
    convert_urls_to_js_array(input_file)

