import { ItemResult } from "@common/enum/item-result.enum"
import { Nullable } from "@common/lib/nullable";
import { ItemStatus } from "./item-status.interface";
import { JobStatus } from "@common/enum/job-status.enum";

export interface JobSummary {
    job_id: string;
    status: JobStatus;
    pushed_at: Date;
    completed_at: Nullable<Date>;
    recount: Record<ItemResult, number>;
    items: Array<ItemStatus>;
}