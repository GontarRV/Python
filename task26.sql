WITH wp_grouped AS (
    SELECT
        wp.workshop_id AS w_id,
        COALESCE(SUM(wp.quantity), 0) AS total_quantity,
        MIN(wp.production_date) AS min_produced_day,
        MAX(wp.production_date) AS max_produced_day,
        COALESCE(SUM(p.value), 0) AS total_value
    FROM
        WORKSHOP_PRODUCTS wp
    LEFT JOIN
        PRODUCTS p ON p.product_id = wp.product_id
    GROUP BY 
        wp.workshop_id
),  
w_grouped AS (
    SELECT
        w.workshop_id AS w_id,
        w.name AS w_name,
        w.type AS w_type,
        w.quality AS w_qual,
        COALESCE(COUNT(wc.dwarf_id), 0) AS w_dwar,
        COALESCE(SUM(wm.quantity), 1) AS material_quntity,
        COALESCE(SUM(dw_lvl_grouped.dw_lvl), 0) AS lvl_SUM
    FROM
        WORKSHOPS w
    LEFT JOIN
        WORKSHOP_CRAFTSDWARVES wc ON wc.workshop_id = w.workshop_id
    LEFT JOIN
        (SELECT
             d.dwarf_id AS dw_id,
             ds.level AS dw_lvl
         FROM
             DWARVES d
         LEFT JOIN
            DWARF_SKILLS ds ON ds.dwarf_id = d.dwarf_id) AS dw_lvl_grouped ON dw_lvl_grouped.dw_id = wc.dwarf_id
    LEFT JOIN
        WORKSHOP_MATERIALS wm ON wm.workshop_id = w.workshop_id AND is_input = true
    GROUP BY 
        w_id, w_name, w_type, w_qual

),
    average_skill AS (
        SELECT
            w_grouped.w_id AS id,
            w_grouped.lvl_SUM/COALESCE(w_grouped.w_dwar, 1) AS av_lvl
        FROM w_grouped
    )
SELECT
    wg.w_id AS workshop_id,
    wg.w_name AS workshop_name,
    wg.w_type AS workshop_type,
    wg.w_dwar AS num_craftsdwarves,
    wp_grouped.total_quantity AS total_quantity_produced,
    wp_grouped.total_value AS total_production_value,
    wp_grouped.total_quantity/COALESCE(EXTRACT(DAY FROM (wp_grouped.max_produced_day - wp_grouped.min_produced_day)), 1) AS daily_production_rate,
    wp_grouped.total_value/wg.material_quntity AS value_per_material_unit,
    wp_grouped.total_quantity/wg.material_quntity AS material_conversion_ratio,
    average_skill.av_lvl AS average_craftsdwarf_skill,
    (average_skill.av_lvl/wg.w_qual)*100 AS skill_quality_correlation,
    JSON_OBJECT (
        'craftsdwarf_ids', (
            SELECT JSON_ARRAYAGG(wc1.dwarf_id)
            FROM WORKSHOP_CRAFTSDWARVES wc1
            WHERE wc1.workshop_id = wg.workshop_id
        ),
        'product_ids', (
            SELECT JSON_ARRAYAGG(wp1.product_id)
            FROM WORKSHOP_PRODUCTS wp1
            WHERE wp1.workshop_id = wg.workshop_id
        ),
        'material_ids', (
            SELECT JSON_ARRAYAGG(wm1.material_id)
            FROM WORKSHOP_MATERIALS wm1
            WHERE wm1.workshop_id = wg.workshop_id
        ),
        'project_ids', (
            SELECT JSON_ARRAYAGG(pr1.project_id)
            FROM PROJECTS pr1
            WHERE pr1.workshop_id = wg.workshop_id
        )
    ) AS related_entities
FROM
    w_grouped wg
LEFT JOIN
    wp_grouped ON wp_grouped.w_id = wg.w_id
LEFT JOIN
    average_skill ON average_skill.id = wg.w_id