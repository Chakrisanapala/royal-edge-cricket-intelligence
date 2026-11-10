const API_BASE = '/api';

export interface OverviewData {
  matches_analyzed: number;
  deliveries_analyzed: number;
  mapped_players: number;
  coverage_period: string;
  high_pressure_deliveries: number;
  high_pressure_pct: number;
  extreme_pressure_pct: number;
  normal_leverage_pct: number;
  top_batters_preview: any[];
  top_bowlers_preview: any[];
  actionable_bowlers_preview: any[];
  simulated_purse_capacity_cr: number;
  total_purse_cr: number;
  overseas_slots_available: string;
  squad_slots: string;
}

export interface Batter {
  rank: number;
  player_id: number;
  player_name: string;
  team: string;
  batting_role: string;
  matches_analyzed: number;
  pressure_innings: number;
  pressure_balls_faced: number;
  pressure_runs_scored: number;
  pressure_batting_avg: number;
  pressure_strike_rate: number;
  death_strike_rate: number;
  chase_strike_rate: number;
  delta_strike_rate_vs_normal: number;
  bootstrap_95_ci_lower_sr: number;
  bootstrap_95_ci_upper_sr: number;
  bootstrap_standard_error_sr: number;
  bpri_score: number;
  sample_size_saturation_index_pct: number;
  uncertainty_interpretation: string;
  ipl_auction_eligibility: string;
}

export interface Bowler {
  rank: number;
  player_id: number;
  player_name: string;
  team: string;
  bowling_role: string;
  matches_analyzed: number;
  pressure_innings: number;
  pressure_overs_bowled: number;
  pressure_legal_balls: number;
  pressure_runs_conceded: number;
  pressure_wickets: number;
  pressure_bowling_avg: number;
  pressure_economy_rate: number;
  pressure_bowling_strike_rate: number;
  death_economy_rate: number;
  delta_economy_vs_normal: number;
  bootstrap_95_ci_lower_econ: number;
  bootstrap_95_ci_upper_econ: number;
  bootstrap_standard_error_econ: number;
  bowpri_score: number;
  sample_size_saturation_index_pct: number;
  uncertainty_interpretation: string;
  ipl_auction_eligibility: string;
}

export interface CompareResult {
  player_type: 'batter' | 'bowler';
  player_a: {
    player_id: number;
    name: string;
    team: string;
    score: number;
    ci: [number, number];
    sssi: number;
  };
  player_b: {
    player_id: number;
    name: string;
    team: string;
    score: number;
    ci: [number, number];
    sssi: number;
  };
  ci_overlap: boolean;
  uncertainty_note: string;
  radar_data: Array<{
    metric: string;
    player_a: number;
    player_b: number;
    val_a: number;
    val_b: number;
  }>;
  deltas: {
    score_delta: number;
    [key: string]: number;
  };
}

export const api = {
  async getOverview(): Promise<OverviewData> {
    const res = await fetch(`${API_BASE}/overview`);
    if (!res.ok) throw new Error('Failed to load overview data');
    return res.json();
  },

  async getBatters(role?: string, search?: string, sortBy = 'bpri_score', ascending = false): Promise<Batter[]> {
    const params = new URLSearchParams();
    if (role) params.append('role', role);
    if (search) params.append('search', search);
    params.append('sort_by', sortBy);
    params.append('ascending', String(ascending));
    const res = await fetch(`${API_BASE}/players/batters?${params.toString()}`);
    if (!res.ok) throw new Error('Failed to load batters');
    return res.json();
  },

  async getBowlers(actionableOnly = false, search?: string, sortBy = 'bowpri_score', ascending = false): Promise<Bowler[]> {
    const params = new URLSearchParams();
    params.append('actionable_only', String(actionableOnly));
    if (search) params.append('search', search);
    params.append('sort_by', sortBy);
    params.append('ascending', String(ascending));
    const res = await fetch(`${API_BASE}/players/bowlers?${params.toString()}`);
    if (!res.ok) throw new Error('Failed to load bowlers');
    return res.json();
  },

  async getPlayerProfile(playerId: number): Promise<any> {
    const res = await fetch(`${API_BASE}/players/${playerId}`);
    if (!res.ok) throw new Error(`Player ${playerId} not found`);
    return res.json();
  },

  async comparePlayers(playerAId: number, playerBId: number, playerType: 'batter' | 'bowler'): Promise<CompareResult> {
    const res = await fetch(`${API_BASE}/compare?player_a_id=${playerAId}&player_b_id=${playerBId}&player_type=${playerType}`);
    if (!res.ok) throw new Error('Failed to compare players');
    return res.json();
  },

  async getPressureSummary(): Promise<any> {
    const res = await fetch(`${API_BASE}/pressure/summary`);
    if (!res.ok) throw new Error('Failed to load pressure summary');
    return res.json();
  },

  async getAuctionTargets(): Promise<any[]> {
    const res = await fetch(`${API_BASE}/auction/targets`);
    if (!res.ok) throw new Error('Failed to load auction targets');
    return res.json();
  },

  async simulateAuction(remainingPurse: number, bids: Record<string, number>): Promise<any> {
    const res = await fetch(`${API_BASE}/auction/simulate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ remaining_purse: remainingPurse, bids })
    });
    if (!res.ok) throw new Error('Failed to run auction simulation');
    return res.json();
  },

  async getMethodology(): Promise<any> {
    const res = await fetch(`${API_BASE}/methodology`);
    if (!res.ok) throw new Error('Failed to load methodology');
    return res.json();
  }
};

