from datetime import datetime
from typing import Any, Literal

class OdooProduct:
    account_tag_ids: Any | Literal[False] # many2many
    active: bool | Literal[False]
    activity_calendar_event_id: Any | Literal[False] # many2one
    activity_date_deadline: datetime | Literal[False]
    activity_exception_decoration: str | Literal[False] # selection
    activity_exception_icon: str | Literal[False]
    activity_ids: Any | Literal[False] # one2many
    activity_state: str | Literal[False] # selection
    activity_summary: str | Literal[False]
    activity_type_icon: str | Literal[False]
    activity_type_id: Any | Literal[False] # many2one
    activity_user_id: Any | Literal[False] # many2one
    additional_product_tag_ids: Any | Literal[False] # many2many
    all_product_tag_ids: Any | Literal[False] # many2many
    attribute_line_ids: Any | Literal[False] # one2many
    available_in_pos: bool | Literal[False]
    avg_cost: float | Literal[False]
    barcode: str | Literal[False]
    can_image_1024_be_zoomed: bool | Literal[False]
    can_image_variant_1024_be_zoomed: bool | Literal[False]
    categ_id: Any # many2one
    code: str | Literal[False]
    color: int | Literal[False]
    combination_indices: str | Literal[False]
    combo_ids: Any | Literal[False] # many2many
    commodity_code_id: Any | Literal[False] # many2one
    company_currency_id: Any | Literal[False] # many2one
    company_id: Any | Literal[False] # many2one
    cost_currency_id: Any | Literal[False] # many2one
    cost_method: str | Literal[False] # selection
    create_date: datetime | Literal[False]
    create_uid: Any | Literal[False] # many2one
    currency_id: Any | Literal[False] # many2one
    default_code: str | Literal[False]
    description: str | Literal[False]
    description_picking: str | Literal[False]
    description_pickingin: str | Literal[False]
    description_pickingout: str | Literal[False]
    description_purchase: str | Literal[False]
    description_sale: str | Literal[False]
    display_name: str | Literal[False]
    expense_policy: str | Literal[False] # selection
    fiscal_country_codes: str | Literal[False]
    free_qty: float | Literal[False]
    has_available_route_ids: bool | Literal[False]
    has_configurable_attributes: bool | Literal[False]
    has_image: bool | Literal[False]
    has_message: bool | Literal[False]
    id: int | Literal[False]
    image_1024: str | Literal[False]
    image_128: str | Literal[False]
    image_1920: str | Literal[False]
    image_256: str | Literal[False]
    image_512: str | Literal[False]
    image_variant_1024: str | Literal[False]
    image_variant_128: str | Literal[False]
    image_variant_1920: str | Literal[False]
    image_variant_256: str | Literal[False]
    image_variant_512: str | Literal[False]
    incoming_qty: float | Literal[False]
    invoice_policy: str | Literal[False] # selection
    is_favorite: bool | Literal[False]
    is_in_purchase_order: bool | Literal[False]
    is_product_variant: bool | Literal[False]
    is_storable: bool | Literal[False]
    list_price: float | Literal[False]
    location_id: Any | Literal[False] # many2one
    lot_properties_definition: Any | Literal[False] # properties_definition
    lot_valuated: bool | Literal[False]
    lst_price: float | Literal[False]
    message_attachment_count: int | Literal[False]
    message_follower_ids: Any | Literal[False] # one2many
    message_has_error: bool | Literal[False]
    message_has_error_counter: int | Literal[False]
    message_has_sms_error: bool | Literal[False]
    message_ids: Any | Literal[False] # one2many
    message_is_follower: bool | Literal[False]
    message_needaction: bool | Literal[False]
    message_needaction_counter: int | Literal[False]
    message_partner_ids: Any | Literal[False] # many2many
    mmd_id: str | Literal[False]
    my_activity_date_deadline: datetime | Literal[False]
    name: str
    nbr_moves_in: int | Literal[False]
    nbr_moves_out: int | Literal[False]
    nbr_reordering_rules: int | Literal[False]
    on_sale_price: float | Literal[False]
    optional_product_ids: Any | Literal[False] # many2many
    orderpoint_ids: Any | Literal[False] # one2many
    outgoing_qty: float | Literal[False]
    packaging_ids: Any | Literal[False] # one2many
    partner_ref: str | Literal[False]
    pos_categ_ids: Any | Literal[False] # many2many
    price_extra: float | Literal[False]
    pricelist_item_count: int | Literal[False]
    pricer_display_price: str | Literal[False]
    pricer_product_to_create_or_update: bool | Literal[False]
    pricer_sale_pricelist_id: Any | Literal[False] # many2one
    pricer_store_id: Any | Literal[False] # many2one
    pricer_tag_ids: Any | Literal[False] # one2many
    product_catalog_product_is_in_sale_order: bool | Literal[False]
    product_document_count: int | Literal[False]
    product_document_ids: Any | Literal[False] # one2many
    product_properties: Any | Literal[False] # properties
    product_tag_ids: Any | Literal[False] # many2many
    product_template_attribute_value_ids: Any | Literal[False] # many2many
    product_template_variant_value_ids: Any | Literal[False] # many2many
    product_tmpl_id: Any # many2one
    product_tooltip: str | Literal[False]
    product_variant_count: int | Literal[False]
    product_variant_id: Any | Literal[False] # many2one
    product_variant_ids: Any # one2many
    property_account_creditor_price_difference: Any | Literal[False] # many2one
    property_account_expense_id: Any | Literal[False] # many2one
    property_account_income_id: Any | Literal[False] # many2one
    property_stock_inventory: Any | Literal[False] # many2one
    property_stock_production: Any | Literal[False] # many2one
    public_description: str | Literal[False]
    purchase_line_warn: str # selection
    purchase_line_warn_msg: str | Literal[False]
    purchase_method: str | Literal[False] # selection
    purchase_ok: bool | Literal[False]
    purchase_order_line_ids: Any | Literal[False] # one2many
    purchased_product_qty: float | Literal[False]
    putaway_rule_ids: Any | Literal[False] # one2many
    qty_available: float | Literal[False]
    quantity_svl: float | Literal[False]
    reordering_max_qty: float | Literal[False]
    reordering_min_qty: float | Literal[False]
    responsible_id: Any | Literal[False] # many2one
    route_from_categ_ids: Any | Literal[False] # many2many
    route_ids: Any | Literal[False] # many2many
    sale_delay: int | Literal[False]
    sale_line_warn: str # selection
    sale_line_warn_msg: str | Literal[False]
    sale_ok: bool | Literal[False]
    sales_count: float | Literal[False]
    seller_ids: Any | Literal[False] # one2many
    sequence: int | Literal[False]
    service_to_purchase: bool | Literal[False]
    service_tracking: str # selection
    service_type: str | Literal[False] # selection
    show_forecasted_qty_status_button: bool | Literal[False]
    show_on_hand_qty_status_button: bool | Literal[False]
    standard_price: float | Literal[False]
    stock_move_ids: Any | Literal[False] # one2many
    stock_quant_ids: Any | Literal[False] # one2many
    stock_valuation_layer_ids: Any | Literal[False] # one2many
    storage_category_capacity_ids: Any | Literal[False] # one2many
    supplier_taxes_id: Any | Literal[False] # many2many
    tax_string: str | Literal[False]
    taxes_id: Any | Literal[False] # many2many
    to_weight: bool | Literal[False]
    total_value: float | Literal[False]
    tracking: str # selection
    type: str # selection
    uom_category_id: Any | Literal[False] # many2one
    uom_id: Any # many2one
    uom_name: str | Literal[False]
    uom_po_id: Any # many2one
    valid_ean: bool | Literal[False]
    valid_product_template_attribute_line_ids: Any | Literal[False] # many2many
    valuation: str | Literal[False] # selection
    value_svl: float | Literal[False]
    variant_seller_ids: Any | Literal[False] # one2many
    virtual_available: float | Literal[False]
    visible_expense_policy: bool | Literal[False]
    volume: float | Literal[False]
    volume_uom_name: str | Literal[False]
    warehouse_id: Any | Literal[False] # many2one
    website_message_ids: Any | Literal[False] # one2many
    weight: float | Literal[False]
    weight_uom_name: str | Literal[False]
    write_date: datetime | Literal[False]
    write_uid: Any | Literal[False] # many2one
