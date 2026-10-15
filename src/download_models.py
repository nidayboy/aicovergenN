from pathlib import Path
import requests
import urllib3.util.connection as urllib3_cn
from tqdm import tqdm

urllib3_cn.HAS_IPV6 = False

MDX_DOWNLOAD_LINK = 'https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/'
RVC_DOWNLOAD_LINK = 'https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/'

BASE_DIR = Path(__file__).resolve().parent.parent
mdxnet_models_dir = BASE_DIR / 'mdxnet_models'
rvc_models_dir = BASE_DIR / 'rvc_models'


def dl_model(link, model_name, dir_name):
    target_path = dir_name / model_name
    if target_path.exists() and target_path.stat().st_size > 1024 * 1024:
        print(f'{model_name} already exists. Skipping download.')
        return
    with requests.get(f'{link}{model_name}', stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get('content-length', 0))
        with open(target_path, 'wb') as f, tqdm(
            desc=model_name,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for chunk in r.iter_content(chunk_size=65536):
                if chunk:
                    size = f.write(chunk)
                    bar.update(size)


if __name__ == '__main__':
    mdx_model_names = ['UVR-MDX-NET-Voc_FT.onnx', 'UVR_MDXNET_KARA_2.onnx', 'Reverb_HQ_By_FoxJoy.onnx']
    for model in mdx_model_names:
        print(f'Downloading {model}...')
        dl_model(MDX_DOWNLOAD_LINK, model, mdxnet_models_dir)

    rvc_model_names = ['hubert_base.pt', 'rmvpe.pt']
    for model in rvc_model_names:
        print(f'Downloading {model}...')
        dl_model(RVC_DOWNLOAD_LINK, model, rvc_models_dir)

    print('All models downloaded!')
