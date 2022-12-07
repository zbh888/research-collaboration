from grobid_client.grobid_client import GrobidClient

if __name__ == "__main__":
    client = GrobidClient(config_path="./grobid_client_python/config.json")
    client.process("processHeaderDocument", "./pdfs", output="./pdfs/xml", tei_coordinates=True, force=True)
