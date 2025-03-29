def rectangles_overlap(r1, r2):
    x1, y1, w1, h1 = r1
    x2, y2, w2, h2 = r2

    r1_x2 = x1 + w1
    r1_y2 = y1 + h1
    r2_x2 = x2 + w2
    r2_y2 = y2 + h2

    inter_x1 = max(x1, x2)
    inter_y1 = max(y1, y2)
    inter_x2 = min(r1_x2, r2_x2)
    inter_y2 = min(r1_y2, r2_y2)

    if inter_x1 < inter_x2 and inter_y1 < inter_y2:
        area_inter = (inter_x2 - inter_x1) * (inter_y2 - inter_y1)
        area_r1 = w1 * h1
        area_r2 = w2 * h2
        return area_inter / min(area_r1, area_r2) > 0.5

    return False