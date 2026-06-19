import os
import zipfile

def zip_dir(src_dir, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(src_dir):
            if '__pycache__' in root:
                continue
            for file in files:
                if file.endswith('.pyc') or file == '.DS_Store':
                    continue
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, os.path.dirname(src_dir))
                # Kodi requires forward slashes
                arcname = rel_path.replace(os.sep, '/')
                zipf.write(abs_path, arcname)

# plugin
plugin_src = r"e:\plugin.video.vietmediaF"
plugin_zips = [
    r"e:\Project\kodi.vietmediaf.store\plugin.video.vietmediaF-11.37.5.3.zip",
    r"e:\Project\kodi.vietmediaf.store\plugin.video.vietmediaF\plugin.video.vietmediaF-11.37.5.3.zip"
]
for p in plugin_zips:
    zip_dir(plugin_src, p)

# repo
repo_src = r"e:\Project\kodi.vietmediaf.store\repo_vietmediaf_fork"
repo_zips = [
    r"e:\Project\kodi.vietmediaf.store\repo_vietmediaf_fork-0.0.3.zip"
]
for p in repo_zips:
    zip_dir(repo_src, p)
