from app.model.odoo.base_model import BaseModel
from datetime import datetime
from typing import Any

class Odoo_ProductProduct(BaseModel):
    activity_ids: Any # one2many
    activity_state: Any # selection
    activity_user_id: Any # many2one
    activity_type_id: Any # many2one
    activity_type_icon: str
    activity_date_deadline: datetime
    my_activity_date_deadline: datetime
    activity_summary: str
    activity_exception_decoration: Any # selection
    activity_exception_icon: str
    activity_calendar_event_id: Any # many2one
    message_is_follower: bool
    message_follower_ids: Any # one2many
    message_partner_ids: Any # many2many
    message_ids: Any # one2many
    has_message: bool
    message_needaction: bool
    message_needaction_counter: int
    message_has_error: bool
    message_has_error_counter: int
    message_attachment_count: int
    website_message_ids: Any # one2many
    message_has_sms_error: bool
    price_extra: float
    lst_price: float
    default_code: str
    code: str
    partner_ref: str
    active: bool
    product_tmpl_id: Any # many2one
    barcode: str
    product_template_attribute_value_ids: Any # many2many
    product_template_variant_value_ids: Any # many2many
    combination_indices: str
    is_product_variant: bool
    standard_price: float
    volume: float
    weight: float
    pricelist_item_count: int
    product_document_ids: Any # one2many
    product_document_count: int
    packaging_ids: Any # one2many
    additional_product_tag_ids: Any # many2many
    all_product_tag_ids: Any # many2many
    image_variant_1920: Any # binary
    image_variant_1024: Any # binary
    image_variant_512: Any # binary
    image_variant_256: Any # binary
    image_variant_128: Any # binary
    can_image_variant_1024_be_zoomed: bool
    image_1920: Any # binary
    image_1024: Any # binary
    image_512: Any # binary
    image_256: Any # binary
    image_128: Any # binary
    can_image_1024_be_zoomed: bool
    write_date: datetime
    id: int
    display_name: str
    create_uid: Any # many2one
    create_date: datetime
    write_uid: Any # many2one
    tax_string: str
    stock_quant_ids: Any # one2many
    stock_move_ids: Any # one2many
    qty_available: float
    virtual_available: float
    free_qty: float
    incoming_qty: float
    outgoing_qty: float
    orderpoint_ids: Any # one2many
    nbr_moves_in: int
    nbr_moves_out: int
    nbr_reordering_rules: int
    reordering_min_qty: float
    reordering_max_qty: float
    putaway_rule_ids: Any # one2many
    storage_category_capacity_ids: Any # one2many
    show_on_hand_qty_status_button: bool
    show_forecasted_qty_status_button: bool
    valid_ean: bool
    lot_properties_definition: Any # properties_definition
    purchased_product_qty: float
    is_in_purchase_order: bool
    value_svl: float
    quantity_svl: float
    avg_cost: Any # monetary
    total_value: Any # monetary
    company_currency_id: Any # many2one
    stock_valuation_layer_ids: Any # one2many
    valuation: Any # selection
    cost_method: Any # selection
    has_image: bool
    purchase_order_line_ids: Any # one2many
    sales_count: float
    product_catalog_product_is_in_sale_order: bool
    pricer_store_id: Any # many2one
    pricer_tag_ids: Any # one2many
    pricer_product_to_create_or_update: bool
    pricer_display_price: str
    pricer_sale_pricelist_id: Any # many2one
    on_sale_price: float
    name: str
    sequence: int
    description: Any # html
    description_purchase: str
    description_sale: str
    type: Any # selection
    combo_ids: Any # many2many
    service_tracking: Any # selection
    categ_id: Any # many2one
    currency_id: Any # many2one
    cost_currency_id: Any # many2one
    list_price: float
    volume_uom_name: str
    weight_uom_name: str
    sale_ok: bool
    purchase_ok: bool
    uom_id: Any # many2one
    uom_name: str
    uom_category_id: Any # many2one
    uom_po_id: Any # many2one
    company_id: Any # many2one
    seller_ids: Any # one2many
    variant_seller_ids: Any # one2many
    color: int
    attribute_line_ids: Any # one2many
    valid_product_template_attribute_line_ids: Any # many2many
    product_variant_ids: Any # one2many
    product_variant_id: Any # many2one
    product_variant_count: int
    has_configurable_attributes: bool
    product_tooltip: str
    is_favorite: bool
    product_tag_ids: Any # many2many
    product_properties: Any # properties
    taxes_id: Any # many2many
    supplier_taxes_id: Any # many2many
    property_account_income_id: Any # many2one
    property_account_expense_id: Any # many2one
    account_tag_ids: Any # many2many
    fiscal_country_codes: str
    is_storable: bool
    responsible_id: Any # many2one
    property_stock_production: Any # many2one
    property_stock_inventory: Any # many2one
    sale_delay: int
    tracking: Any # selection
    description_picking: str
    description_pickingout: str
    description_pickingin: str
    location_id: Any # many2one
    warehouse_id: Any # many2one
    has_available_route_ids: bool
    route_ids: Any # many2many
    route_from_categ_ids: Any # many2many
    purchase_method: Any # selection
    purchase_line_warn: Any # selection
    purchase_line_warn_msg: str
    lot_valuated: bool
    mmd_id: str
    available_in_pos: bool
    to_weight: bool
    pos_categ_ids: Any # many2many
    public_description: str
    property_account_creditor_price_difference: Any # many2one
    service_type: Any # selection
    sale_line_warn: Any # selection
    sale_line_warn_msg: str
    expense_policy: Any # selection
    visible_expense_policy: bool
    invoice_policy: Any # selection
    optional_product_ids: Any # many2many
    service_to_purchase: bool
    commodity_code_id: Any # many2one