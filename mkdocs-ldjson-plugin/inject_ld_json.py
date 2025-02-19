import json
from mkdocs.plugins import BasePlugin
from bs4 import BeautifulSoup

class InjectLDJsonPlugin(BasePlugin):
    def on_post_page(self, output, page, config):
        """Inject JSON-LD metadata into the <head> section of the rendered page."""
        
        # Get JSON-LD data from page metadata
        json_ld = page.meta.get("json_ld")
        if not json_ld:
            return output  # No JSON-LD to inject, return page as is
        
        # Convert dictionary to JSON string
        json_ld_str = json.dumps(json_ld, indent=2)

        # Parse the HTML output
        soup = BeautifulSoup(output, "html.parser")
        
        # Create <script> tag for JSON-LD
        script_tag = soup.new_tag("script", type="application/ld+json")
        script_tag.string = json_ld_str

        # Find the <head> and insert the script
        if soup.head:
            soup.head.append(script_tag)

        return str(soup)