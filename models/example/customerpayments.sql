with customer_source as (
    select *
    from {{ source('rentals', 'customer') }}
),
customer_payment as (
    select *
    from {{ source('rentals', 'payment') }}
)
select customer_source.email,
    customer_payment.payment_id,
    customer_payment.amount,
    customer_payment.payment_date,
    date(customer_payment.payment_date) as transaction_date
from customer_source
    inner join customer_payment on customer_source.customer_id = customer_payment.customer_id
