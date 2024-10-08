import cv2

from ccrestoration import AutoConfig, AutoModel, BaseConfig, ConfigType
from ccrestoration.model import SRBaseModel

from .util import ASSETS_PATH, calculate_image_similarity, compare_image_size, get_device, load_image


class Test_RealESRGAN:
    def test_official(self) -> None:
        img1 = load_image()

        for k in [
            ConfigType.RealESRGAN_RealESRGAN_x4plus_4x,
            ConfigType.RealESRGAN_RealESRGAN_x4plus_anime_6B_4x,
            ConfigType.RealESRGAN_RealESRGAN_x2plus_2x,
            ConfigType.RealESRGAN_realesr_animevideov3_4x,
        ]:
            print(f"Testing {k}")
            cfg: BaseConfig = AutoConfig.from_pretrained(k)
            model: SRBaseModel = AutoModel.from_config(config=cfg, fp16=False, device=get_device())
            print(model.device)

            img2 = model.inference_image(img1)
            cv2.imwrite(str(ASSETS_PATH / f"test_{k}_out.jpg"), img2)

            assert calculate_image_similarity(img1, img2)
            assert compare_image_size(img1, img2, cfg.scale)

    def test_custom(self) -> None:
        img1 = load_image()

        for k in [
            ConfigType.RealESRGAN_AnimeJaNai_HD_V3_Compact_2x,
            ConfigType.RealESRGAN_AniScale_2_Compact_2x,
            ConfigType.RealESRGAN_Ani4Kv2_Compact_2x,
            ConfigType.RealESRGAN_APISR_RRDB_GAN_generator_2x,
            ConfigType.RealESRGAN_APISR_RRDB_GAN_generator_4x,
        ]:
            print(f"Testing {k}")
            cfg: BaseConfig = AutoConfig.from_pretrained(k)
            model: SRBaseModel = AutoModel.from_config(config=cfg, fp16=False, device=get_device())
            print(model.device)

            img2 = model.inference_image(img1)
            cv2.imwrite(str(ASSETS_PATH / f"test_{k}_out.jpg"), img2)

            assert calculate_image_similarity(img1, img2, 0.8)
            assert compare_image_size(img1, img2, cfg.scale)
