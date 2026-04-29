import { ItemResult } from "@common/enum/item-result.enum"

export interface ItemStatus {
    item_id: string;
    row_id: string;
    result: ItemResult;
}