select
    date,
    name,
    amount
from {{ source('payments', 'payments') }}