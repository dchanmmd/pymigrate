import { ItemResult } from "../enum/item-result.enum";
import { ItemStatus } from "./item-status.interface";

export interface JobSummary {
    job_id: string;
    status: string;
    pushed_at: Date;
    completed_at: Date | null;
    recount: Record<ItemResult, number>;
    items: Array<ItemStatus>;
}
