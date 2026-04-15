import sys
import json
import re
import urllib.request

def format_authors_ipb(authors_list):
    """
    Format list penulis menjadi Gaya IPB: NamaKeluarga II (tanpa titik).
    Max 10 penulis, lebih dari itu pakai et al.
    """
    formatted = []
    for i, auth in enumerate(authors_list):
        if i >= 10:
            return ", ".join(formatted) + ", et al."
        
        # Asumsi format input: "First Middle Last" atau "Last, First Middle"
        if "," in auth:
            last, first = auth.split(",", 1)
            last = last.strip()
            initials = "".join([n[0].upper() for n in first.split()])
        else:
            parts = auth.split()
            last = parts[-1]
            initials = "".join([n[0].upper() for n in parts[:-1]])
        
        formatted.append(f"{last} {initials}")
    
    return ", ".join(formatted)

def fetch_doi_metadata(doi):
    """Mengambil metadata jurnal via CrossRef API."""
    url = f"https://api.crossref.org/works/{doi}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'PPKI-IPB-Agent/1.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            item = data['message']
            
            authors = [f"{a.get('family', '')}, {a.get('given', '')}" for a in item.get('author', [])]
            title = item.get('title', [''])[0]
            journal = item.get('container-title', [''])[0]
            year = item.get('published-print', item.get('published-online', {'date-parts': [[0]]}))['date-parts'][0][0]
            volume = item.get('volume', '')
            issue = item.get('issue', '')
            pages = item.get('page', '')
            
            return {
                "authors": authors,
                "year": year,
                "title": title,
                "journal": journal,
                "volume": volume,
                "issue": issue,
                "pages": pages,
                "doi": doi
            }
    except Exception as e:
        return None

def generate_citation(doi):
    meta = fetch_doi_metadata(doi)
    if not meta:
        return f"❌ Gagal mengambil metadata untuk DOI: {doi}"
    
    # Apply IPB Rules
    authors = format_authors_ipb(meta['authors'])
    title = meta['title'].capitalize() # Sentence case
    journal = meta['journal'] # In reality should be abbreviated, but we keep full for now
    
    vol_iss = f"{meta['volume']}"
    if meta['issue']:
        vol_iss += f"({meta['issue']})"
    
    citation = f"{authors}. {meta['year']}. {title}. *{journal}*. {vol_iss}:{meta['pages']}. doi:{doi}."
    return citation

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cite_ppki.py <DOI>")
        sys.exit(1)
    
    doi_input = sys.argv[1].replace("https://doi.org/", "")
    print(f"📖 Menghasilkan Sitasi IPB (DOI: {doi_input})...")
    print("-" * 60)
    print(generate_citation(doi_input))
