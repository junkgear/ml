from sourced.ml.algorithms import NoopTokenParser
from sourced.ml.algorithms.uast_ids_to_bag import UastIds2Bag
from sourced.ml.extractors import BagsExtractor, register_extractor


@register_extractor
class IdentifiersBagExtractor(BagsExtractor):
    NAME = "id"
    NAMESPACE = "i."
    OPTS = {"split-stem": True}
    OPTS.update(BagsExtractor.OPTS)

    def __init__(self, docfreq_threshold=None, split_stem=True, **kwargs):
        super().__init__(docfreq_threshold, **kwargs)
        self.id2bag = UastIds2Bag(None, NoopTokenParser() if not split_stem else None)

    def uast_to_bag(self, uast):
        return self.id2bag(uast)
