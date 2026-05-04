export interface InventoryItem {
    internal_ref: string;
    barcode: string;
    name: string;
    description: string;
    uom: string;
    purchase_uom: string;
    weight: number;
    carat_rating: string;
    can_be_sold: boolean;
    can_be_bought: boolean;
    product_type: string;
    provider_tax: string;
    customer_tax: string;
    tags: string;
    retail_price: number;
    cost: number;
    observations: string;
    pawn_no: string;
    stone_weight: number;
    brand: string;
    model: string;
    series: string;
    branch: string;
    product_category: string;
}