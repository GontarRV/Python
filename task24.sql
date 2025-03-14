SELECT 
    e.expedition_id,
    e.destination,
    e.status,
    (SELECT round(((SELECT count(*)
                    FROM EXPEDITION_MEMBERS em1
                    WHERE em1.expedition_id = e.expedition_id and em1.survived = true) :: numeric / count(*)) * 100, 2)
        FROM EXPEDITION_MEMBERS em
        WHERE em.expedition_id = e.expedition_id) AS survival_rate,
    (SELECT sum(ea.value) 
        FROM EXPEDITION_ARTIFACTS ea 
        WHERE ea.expedition_id = e.expedition_id) AS artifacts_value,
    (SELECT count(*) 
        FROM EXPEDITION_SITES es 
        WHERE es.expedition_id = e.expedition_id) AS discovered_sites,
    (SELECT round(((SELECT count(*)
                    FROM EXPEDITION_CREATURES ec1
                    WHERE ec1.expedition_id = e.expedition_id and ec1.outcome = 'success') :: numeric / count(*)) * 100, 2)
        FROM EXPEDITION_CREATURES ec
        WHERE ec.expedition_id = e.expedition_id) AS encounter_success_rate,
    DATEDIFF (day, e.departure_date, e.return_date) AS expedition_duration,
    JSON_OBJECT (
        'member_ids', (
            SELECT JSON_ARRAYAGG(eml.dwarf_id)
            FROM EXPEDITION_MEMBERS eml
            WHERE eml.expedition_id = e.expedition_id
        ),
        'artifact_ids', (
            SELECT JSON_ARRAYAGG(eal.artifact_id)
            FROM EXPEDITION_ARTIFACTS eal
            WHERE eal.expedition_id = e.expedition_id
        ),
        'site_ids', (
            SELECT JSON_ARRAYAGG(esl.site_id)
            FROM EXPEDITION_SITES esl
            WHERE esl.expedition_id = e.expedition_id
        )
    ) AS related_entities
FROM EXPEDITIONS e;