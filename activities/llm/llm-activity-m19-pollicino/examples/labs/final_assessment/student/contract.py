"""Public output contract. Shape/provenance checks do not establish truth."""


def validate(result, source_ids):
    if not isinstance(result, dict) or set(result) != {"id", "abstained", "points"}:
        raise ValueError("required keys: id, abstained, points")
    if not isinstance(result["id"], str) or type(result["abstained"]) is not bool:
        raise ValueError("id must be a string and abstained a boolean")
    points = result["points"]
    if not isinstance(points, list) or len(points) != (0 if result["abstained"] else 3):
        raise ValueError("zero points when abstaining, otherwise exactly three")
    seen = set()
    for point in points:
        if not isinstance(point, dict) or set(point) != {"testo", "source_id"}:
            raise ValueError("point requires testo and source_id")
        if not isinstance(point["testo"], str) or not point["testo"].strip():
            raise ValueError("nonempty text required")
        source = point["source_id"]
        if not isinstance(source, str) or source not in source_ids or source in seen:
            raise ValueError("source must be available to this case and used only once")
        seen.add(source)
    return result
