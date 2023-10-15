select distinct
    payment_id
from {{ ref('customerpayments') }}
where amount < 0