<template>
  <div class="app-container" style="padding-left: 40px">
    <!--    <p>{{ roles }}</p>-->
    <el-row :gutter="20">
      <el-col :span="16">
        <div class="grid-content bg-purple">
          <!--    表单-->
          <el-form :inline="true" :model="formInline" class="demo-form-inline">
            <el-form-item label="起点">
              <el-select v-model="formInline.start" placeholder="起点">
                <el-option v-for="item in locations" :key="item.id" :lable="item.id" :value="item.name" />
              </el-select>
            </el-form-item>
            <el-form-item label="终点">
              <el-select v-model="formInline.end" placeholder="终点">
                <el-option v-for="item in locations" :key="item.id" :lable="item.id" :value="item.name" />
              </el-select>
            </el-form-item>
            <el-form-item>
              <span class="demonstration">日期</span>
              <el-date-picker
                v-model="formInline.time"
                align="right"
                type="date"
                placeholder="选择日期"
                format="yyyy 年 MM 月 dd 日"
                value-format="yyyy-MM-dd"
                :picker-options="pickerOptions"
              />
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit">查询</el-button>

              <!--              <el-button type="primary" @click="searchFlightLess">time</el-button>-->
              <!--              <el-button type="primary" @click="onSubmit">ticket</el-button>-->
              <!--              <el-button type="primary" @click="onSubmit">money</el-button>-->
            </el-form-item>
          </el-form>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="grid-content bg-purple">
          <!--    根据flightnumber查询-->
          <el-form :inline="true" class="demo-form-inline">
            <el-form-item label="航班号">
              <el-input
                v-model="flightNumber"
                style="width: 220px"
                placeholder="航班号"
                @keyup.enter.native="SubmitByFlightNumber"
              />
              <el-button type="primary" @click="SubmitByFlightNumber">查询</el-button>

            </el-form-item>
          </el-form>
        </div>
      </el-col>
    </el-row>
    <template>
      <el-tabs :tab-position="tabPosition" style="height: 500px" @tab-click="changemethed">
        <el-tab-pane label="direct"><el-table
          v-if="list"
          v-loading="loading"
          :data="list"
          border
          fit
          :default-sort="{prop: 'id'}"
          @sort-change="FlightSort"
        >
          <el-table-column align="center" label="ID" prop="id" sortable>
            <template slot-scope="scope">
              {{ scope.row.id }}
            </template>
          </el-table-column>
          <el-table-column label="航空公司" prop="airId" sortable>
            <template slot-scope="scope">
              {{ scope.row.airId }}
            </template>
          </el-table-column>
          <el-table-column label="航班号" align="center" prop="flightNumber" sortable>
            <template slot-scope="scope">
              <span>{{ scope.row.flightNumber }}</span>
            </template>
          </el-table-column>
          <el-table-column label="起点" align="center" sortable prop="startlocationId">
            <template slot-scope="scope">
              <span>{{ scope.row.startlocationId }}</span>
            </template>
          </el-table-column>
          <el-table-column label="出发时间" width="180" align="center" prop="startTime" sortable="custom">
            <template slot-scope="scope">
              <i class="el-icon-time" />
              <span>{{ scope.row.startTime }}</span>
            </template>
          </el-table-column>
          <el-table-column label="终点" align="center" prop="endTime" sortable>
            <template slot-scope="scope">
              {{ scope.row.endlocationId }}
            </template>
          </el-table-column>
          <el-table-column label="到达时间" width="180" align="center" prop="endTime" sortable>
            <template slot-scope="scope">
              <i class="el-icon-time" />
              <span>{{ scope.row.endTime }}</span>
            </template>
          </el-table-column>
          <el-table-column label="时长" align="center" sortable prop="estimateTime">
            <template slot-scope="scope">
              <span>{{ scope.row.estimateTime }}</span>
            </template>
          </el-table-column>
          <el-table-column label="价格" align="center" prop="price" sortable>
            <template slot-scope="scope">
              <span>{{ scope.row.price }}</span>
            </template>
          </el-table-column>
          <el-table-column label="余票" align="center" prop="ticket" sortable>
            <template slot-scope="scope">
              <span>{{ scope.row.ticket }}</span>
            </template>
          </el-table-column>
          <el-table-column label="状态" align="center" prop="condition" sortable>
            <template slot-scope="scope">
              <el-tag :type="scope.row.condition | statusformFilter">{{ scope.row.condition| msgformFilter }}</el-tag>
              <!--            <span>{{ scope.row.condition }}</span>-->
            </template>
          </el-table-column>
          <el-table-column label="操作" width="180px">
            <!--          子表格-->
            <template slot-scope="scope">
              <el-popover
                v-if="scope.row.stop == '' ? false : true"
                placement="right"
                trigger="hover"
              >
                <el-table :data="scope.row.stop">
                  <el-table-column label="经停地点" align="center">
                    <template slot-scope="scope">
                      <span>{{ scope.row.location }}</span>
                    </template>
                  </el-table-column>
                </el-table>
                <el-button slot="reference" size="small" type="info" icon="el-icon-s-promotion" />
              </el-popover>
              <!--            点击后转到购买-->
              <el-button v-if="scope.row.condition == 1 ? true : false" type="primary" size="small" icon="el-icon-s-claim" @click="buyFlight(scope.row.id,scope.row.ticket)" />
              <el-button v-if="testshow" type="danger" size="small" icon="el-icon-s-tools" @click="modityflight(scope.$index)" />
            </template>
          </el-table-column>
        </el-table>
        </el-tab-pane>
        <el-tab-pane label="lessprice"><el-table
          v-if="list"
          v-loading="loading"
          :data="list"
          border
          fit
          :default-sort="{prop: 'id'}"
          @sort-change="FlightSort"
        >
          <el-table-column align="center" label="ID" prop="id" sortable>
            <template slot-scope="scope">
              {{ scope.row.id }}
            </template>
          </el-table-column>
          <el-table-column label="航空公司" prop="airId" sortable>
            <template slot-scope="scope">
              {{ scope.row.airId }}
            </template>
          </el-table-column>
          <el-table-column label="航班号" align="center" prop="flightNumber" sortable>
            <template slot-scope="scope">
              <span>{{ scope.row.flightNumber }}</span>
            </template>
          </el-table-column>
          <el-table-column label="起点" align="center" sortable prop="startlocationId">
            <template slot-scope="scope">
              <span>{{ scope.row.startlocationId }}</span>
            </template>
          </el-table-column>
          <el-table-column label="出发时间" width="180" align="center" prop="startTime" sortable="custom">
            <template slot-scope="scope">
              <i class="el-icon-time" />
              <span>{{ scope.row.startTime }}</span>
            </template>
          </el-table-column>
          <el-table-column label="终点" align="center" prop="endTime" sortable>
            <template slot-scope="scope">
              {{ scope.row.endlocationId }}
            </template>
          </el-table-column>
          <el-table-column label="到达时间" width="180" align="center" prop="endTime" sortable>
            <template slot-scope="scope">
              <i class="el-icon-time" />
              <span>{{ scope.row.endTime }}</span>
            </template>
          </el-table-column>
          <el-table-column label="时长" align="center" sortable prop="estimateTime">
            <template slot-scope="scope">
              <span>{{ scope.row.estimateTime }}</span>
            </template>
          </el-table-column>
          <el-table-column label="价格" align="center" prop="price" sortable>
            <template slot-scope="scope">
              <span>{{ scope.row.price }}</span>
            </template>
          </el-table-column>
          <el-table-column label="余票" align="center" prop="ticket" sortable>
            <template slot-scope="scope">
              <span>{{ scope.row.ticket }}</span>
            </template>
          </el-table-column>
          <el-table-column label="状态" align="center" prop="condition" sortable>
            <template slot-scope="scope">
              <el-tag :type="scope.row.condition | statusformFilter">{{ scope.row.condition| msgformFilter }}</el-tag>
              <!--            <span>{{ scope.row.condition }}</span>-->
            </template>
          </el-table-column>
          <el-table-column label="操作" width="180px">
            <!--          子表格-->
            <template slot-scope="scope">
              <el-popover
                v-if="scope.row.stop == '' ? false : true"
                placement="right"
                trigger="hover"
              >
                <el-table :data="scope.row.stop">
                  <el-table-column label="经停地点" align="center">
                    <template slot-scope="scope">
                      <span>{{ scope.row.location }}</span>
                    </template>
                  </el-table-column>
                </el-table>
                <el-button slot="reference" size="small" type="info" icon="el-icon-s-promotion" />
              </el-popover>
              <!--            点击后转到购买-->
              <el-button v-if="scope.row.condition == 1 ? true : false" type="primary" size="small" icon="el-icon-s-claim" @click="buyFlight(scope.row.id,scope.row.ticket)" />
              <el-button v-if="testshow" type="danger" size="small" icon="el-icon-s-tools" @click="modityflight(scope.$index)" />
            </template>
          </el-table-column>
        </el-table>
        </el-tab-pane>
        <el-tab-pane label="lesstime">
          <el-table
            v-if="list"
            v-loading="loading"
            :data="list"
            border
            fit
            :default-sort="{prop: 'id'}"
            @sort-change="FlightSort"
          >
            <el-table-column align="center" label="ID" prop="id" sortable>
              <template slot-scope="scope">
                {{ scope.row.id }}
              </template>
            </el-table-column>
            <el-table-column label="航空公司" prop="airId" sortable>
              <template slot-scope="scope">
                {{ scope.row.airId }}
              </template>
            </el-table-column>
            <el-table-column label="航班号" align="center" prop="flightNumber" sortable>
              <template slot-scope="scope">
                <span>{{ scope.row.flightNumber }}</span>
              </template>
            </el-table-column>
            <el-table-column label="起点" align="center" sortable prop="startlocationId">
              <template slot-scope="scope">
                <span>{{ scope.row.startlocationId }}</span>
              </template>
            </el-table-column>
            <el-table-column label="出发时间" width="180" align="center" prop="startTime" sortable="custom">
              <template slot-scope="scope">
                <i class="el-icon-time" />
                <span>{{ scope.row.startTime }}</span>
              </template>
            </el-table-column>
            <el-table-column label="终点" align="center" prop="endTime" sortable>
              <template slot-scope="scope">
                {{ scope.row.endlocationId }}
              </template>
            </el-table-column>
            <el-table-column label="到达时间" width="180" align="center" prop="endTime" sortable>
              <template slot-scope="scope">
                <i class="el-icon-time" />
                <span>{{ scope.row.endTime }}</span>
              </template>
            </el-table-column>
            <el-table-column label="时长" align="center" sortable prop="estimateTime">
              <template slot-scope="scope">
                <span>{{ scope.row.estimateTime }}</span>
              </template>
            </el-table-column>
            <el-table-column label="价格" align="center" prop="price" sortable>
              <template slot-scope="scope">
                <span>{{ scope.row.price }}</span>
              </template>
            </el-table-column>
            <el-table-column label="余票" align="center" prop="ticket" sortable>
              <template slot-scope="scope">
                <span>{{ scope.row.ticket }}</span>
              </template>
            </el-table-column>
            <el-table-column label="状态" align="center" prop="condition" sortable>
              <template slot-scope="scope">
                <el-tag :type="scope.row.condition | statusformFilter">{{ scope.row.condition| msgformFilter }}</el-tag>
                <!--            <span>{{ scope.row.condition }}</span>-->
              </template>
            </el-table-column>
            <el-table-column label="操作" width="180px">
              <!--          子表格-->
              <template slot-scope="scope">
                <el-popover
                  v-if="scope.row.stop == '' ? false : true"
                  placement="right"
                  trigger="hover"
                >
                  <el-table :data="scope.row.stop">
                    <el-table-column label="经停地点" align="center">
                      <template slot-scope="scope">
                        <span>{{ scope.row.location }}</span>
                      </template>
                    </el-table-column>
                  </el-table>
                  <el-button slot="reference" size="small" type="info" icon="el-icon-s-promotion" />
                </el-popover>
                <!--            点击后转到购买-->
                <el-button v-if="scope.row.condition == 1 ? true : false" type="primary" size="small" icon="el-icon-s-claim" @click="buyFlight(scope.row.id,scope.row.ticket)" />
                <el-button v-if="testshow" type="danger" size="small" icon="el-icon-s-tools" @click="modityflight(scope.$index)" />
              </template>
            </el-table-column>
          </el-table>
        </el-tab-pane>
        <el-tab-pane label="moreticket">
          <el-table
            v-if="list"
            v-loading="loading"
            :data="list"
            border
            fit
            :default-sort="{prop: 'id'}"
            @sort-change="FlightSort"
          >
            <el-table-column align="center" label="ID" prop="id" sortable>
              <template slot-scope="scope">
                {{ scope.row.id }}
              </template>
            </el-table-column>
            <el-table-column label="航空公司" prop="airId" sortable>
              <template slot-scope="scope">
                {{ scope.row.airId }}
              </template>
            </el-table-column>
            <el-table-column label="航班号" align="center" prop="flightNumber" sortable>
              <template slot-scope="scope">
                <span>{{ scope.row.flightNumber }}</span>
              </template>
            </el-table-column>
            <el-table-column label="起点" align="center" sortable prop="startlocationId">
              <template slot-scope="scope">
                <span>{{ scope.row.startlocationId }}</span>
              </template>
            </el-table-column>
            <el-table-column label="出发时间" width="180" align="center" prop="startTime" sortable="custom">
              <template slot-scope="scope">
                <i class="el-icon-time" />
                <span>{{ scope.row.startTime }}</span>
              </template>
            </el-table-column>
            <el-table-column label="终点" align="center" prop="endTime" sortable>
              <template slot-scope="scope">
                {{ scope.row.endlocationId }}
              </template>
            </el-table-column>
            <el-table-column label="到达时间" width="180" align="center" prop="endTime" sortable>
              <template slot-scope="scope">
                <i class="el-icon-time" />
                <span>{{ scope.row.endTime }}</span>
              </template>
            </el-table-column>
            <el-table-column label="时长" align="center" sortable prop="estimateTime">
              <template slot-scope="scope">
                <span>{{ scope.row.estimateTime }}</span>
              </template>
            </el-table-column>
            <el-table-column label="价格" align="center" prop="price" sortable>
              <template slot-scope="scope">
                <span>{{ scope.row.price }}</span>
              </template>
            </el-table-column>
            <el-table-column label="余票" align="center" prop="ticket" sortable>
              <template slot-scope="scope">
                <span>{{ scope.row.ticket }}</span>
              </template>
            </el-table-column>
            <el-table-column label="状态" align="center" prop="condition" sortable>
              <template slot-scope="scope">
                <el-tag :type="scope.row.condition | statusformFilter">{{ scope.row.condition| msgformFilter }}</el-tag>
                <!--            <span>{{ scope.row.condition }}</span>-->
              </template>
            </el-table-column>
            <el-table-column label="操作" width="180px">
              <!--          子表格-->
              <template slot-scope="scope">
                <el-popover
                  v-if="scope.row.stop == '' ? false : true"
                  placement="right"
                  trigger="hover"
                >
                  <el-table :data="scope.row.stop">
                    <el-table-column label="经停地点" align="center">
                      <template slot-scope="scope">
                        <span>{{ scope.row.location }}</span>
                      </template>
                    </el-table-column>
                  </el-table>
                  <el-button slot="reference" size="small" type="info" icon="el-icon-s-promotion" />
                </el-popover>

                <!--            点击后转到购买-->
                <el-button v-if="scope.row.condition == 1 ? true : false" type="primary" size="small" icon="el-icon-s-claim" @click="buyFlight(scope.row.id,scope.row.ticket)" />
                <el-button v-if="testshow" type="danger" size="small" icon="el-icon-s-tools" @click="modityflight(scope.$index)" />

              </template>
            </el-table-column>
          </el-table>
        </el-tab-pane>

        <el-tab-pane label="zonghe">
          <el-table
            v-if="list"
            v-loading="loading"
            :data="list"
            border
            fit
            :default-sort="{prop: 'id'}"
            @sort-change="FlightSort"
          >
            <el-table-column align="center" label="ID" prop="id" sortable>
              <template slot-scope="scope">
                {{ scope.row.id }}
              </template>
            </el-table-column>
            <el-table-column label="航空公司" prop="airId" sortable>
              <template slot-scope="scope">
                {{ scope.row.airId }}
              </template>
            </el-table-column>
            <el-table-column label="航班号" align="center" prop="flightNumber" sortable>
              <template slot-scope="scope">
                <span>{{ scope.row.flightNumber }}</span>
              </template>
            </el-table-column>
            <el-table-column label="起点" align="center" sortable prop="startlocationId">
              <template slot-scope="scope">
                <span>{{ scope.row.startlocationId }}</span>
              </template>
            </el-table-column>
            <el-table-column label="出发时间" width="180" align="center" prop="startTime" sortable="custom">
              <template slot-scope="scope">
                <i class="el-icon-time" />
                <span>{{ scope.row.startTime }}</span>
              </template>
            </el-table-column>
            <el-table-column label="终点" align="center" prop="endTime" sortable>
              <template slot-scope="scope">
                {{ scope.row.endlocationId }}
              </template>
            </el-table-column>
            <el-table-column label="到达时间" width="180" align="center" prop="endTime" sortable>
              <template slot-scope="scope">
                <i class="el-icon-time" />
                <span>{{ scope.row.endTime }}</span>
              </template>
            </el-table-column>
            <el-table-column label="时长" align="center" sortable prop="estimateTime">
              <template slot-scope="scope">
                <span>{{ scope.row.estimateTime }}</span>
              </template>
            </el-table-column>
            <el-table-column label="价格" align="center" prop="price" sortable>
              <template slot-scope="scope">
                <span>{{ scope.row.price }}</span>
              </template>
            </el-table-column>
            <el-table-column label="余票" align="center" prop="ticket" sortable>
              <template slot-scope="scope">
                <span>{{ scope.row.ticket }}</span>
              </template>
            </el-table-column>
            <el-table-column label="状态" align="center" prop="condition" sortable>
              <template slot-scope="scope">
                <el-tag :type="scope.row.condition | statusformFilter">{{ scope.row.condition| msgformFilter }}</el-tag>
                <!--            <span>{{ scope.row.condition }}</span>-->
              </template>
            </el-table-column>
            <el-table-column label="操作" width="180px">
              <!--          子表格-->
              <template slot-scope="scope">
                <el-popover
                  v-if="scope.row.stop == '' ? false : true"
                  placement="right"
                  trigger="hover"
                >
                  <el-table :data="scope.row.stop">
                    <el-table-column label="经停地点" align="center">
                      <template slot-scope="scope">
                        <span>{{ scope.row.location }}</span>
                      </template>
                    </el-table-column>
                  </el-table>
                  <el-button slot="reference" size="small" type="info" icon="el-icon-s-promotion" />
                </el-popover>

                <!--            点击后转到购买-->
                <el-button v-if="scope.row.condition == 1 ? true : false" type="primary" size="small" icon="el-icon-s-claim" @click="buyFlight(scope.row.id,scope.row.ticket)" />
                <el-button v-if="testshow" type="danger" size="small" icon="el-icon-s-tools" @click="modityflight(scope.$index)" />

              </template>
            </el-table-column>
          </el-table>
        </el-tab-pane>
      </el-tabs>

    </template>
    <div v-if="modformvisable">
      <!--        嵌套添加表单-->
      <el-dialog title="修改flight" :visible.sync="modformvisable">
        <el-form :model="flightform">
          <el-card shadow="hover">
            id: {{ flightform.id }}
          </el-card>
          <!--          <el-form-item label="航空公司">-->
          <!--            <el-input v-model="flightform.airId" />-->
          <!--          </el-form-item>-->
          <el-form-item>
            <span class="demonstration"><strong>航空公司</strong></span><br>
            <el-select v-model="flightform.airId">
              <el-option v-for="item in airlinelist" :key="item.id" :lable="item.id" :value="item.name" />
            </el-select>
          </el-form-item>
          <el-form-item label="航班号">
            <el-input v-model="flightform.flightNumber" autocomplete="off" />
          </el-form-item>

          <el-form-item>
            <span class="demonstration"><strong>起点</strong></span><br>
            <el-select v-model="flightform.startlocationId" placeholder="起点">
              <el-option v-for="item in locations" :key="item.id" :lable="item.name" :value="item.name" />
            </el-select>
          </el-form-item>

          <el-form-item>
            <span class="demonstration"><strong>出发时间</strong></span><br>
            <el-date-picker
              v-model="flightform.startTime"
              type="datetime"
              placeholder="选择日期"
              format="yyyy-MM-dd HH:mm"
              value-format="yyyy-MM-dd HH:mm"
              :picker-options="pickerOptions"
            />
          </el-form-item>
          <el-form-item>
            <span class="demonstration"><strong>终点</strong></span><br>
            <el-select v-model="flightform.endlocationId">
              <el-option v-for="item in locations" :key="item.id" :lable="item.name" :value="item.name" />
            </el-select>
          </el-form-item>
          <el-form-item>
            <span class="demonstration"><strong>到达时间</strong></span><br>
            <el-date-picker
              v-model="flightform.endTime"
              type="datetime"
              placeholder="选择日期"
              format="yyyy-MM-dd HH:mm"
              value-format="yyyy-MM-dd HH:mm"
              :picker-options="pickerOptions"
            />
          </el-form-item>
          <el-form-item label="价格">
            <el-input v-model="flightform.price" autocomplete="off" />
          </el-form-item>
          <el-form-item label="余票">
            <el-input v-model="flightform.ticket" autocomplete="off" />
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button type="info" @click="deleteFlightForm">删除</el-button>
          <el-button type="info" @click="addFlightForm">添加</el-button>
          <el-button type="danger" @click="cancelFlight(flightform.id,'延误')">发布延误信息</el-button>
          <el-button type="danger" @click="cancelFlight(flightform.id,'取消')">取消该航班</el-button>
          <el-button @click="modformvisable = false">取消修改</el-button>
          <el-button type="primary" @click="modifyFlightForm">确 定</el-button>

        </div>
      </el-dialog>
      <!--        嵌套添加表单结束-->
    </div>
  </div>
</template>

<script>
import { modifyflightformpost, cancelflight, addflightformpost, deleteflight } from '../../api/manage'
import { searchFlight } from '../../api/flightInformation'
import { getAllLocation, searchByFlightNumber, buywaitpost, buypost, flightorder, getAllAirline, searchflightless } from '../../api/user'
import { getToken } from '@/utils/auth'
export default {
  name: 'Index',
  filters: {
    statusFilter(status) {
      const statusMap = {
        published: 'success',
        draft: 'gray',
        deleted: 'danger'
      }
      return statusMap[status]
    },
    statusformFilter(status) {
      const statusMap = {
        1: 'primary',
        2: 'info',
        0: 'danger'
      }
      return statusMap[status]
    },
    msgformFilter(status) {
      const statusMap = {
        1: 'normal',
        2: 'delay',
        0: 'cancel'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      loading: true,
      tabPosition: 'left',
      list: null,
      listLoading: true,
      flightNumber: '',
      flightform: null,
      modformvisable: false,
      pickerOptions: {
        disabledDate(time) {
          return time.getTime() + 3600 * 1000 * 24 < Date.now()
        },
        shortcuts: [{
          text: '今天',
          onClick(picker) {
            picker.$emit('pick', new Date())
          }
        }, {
          text: '明天',
          onClick(picker) {
            const date = new Date()
            date.setTime(date.getTime() + 3600 * 1000 * 24)
            picker.$emit('pick', date)
          }
        }, {
          text: '后天',
          onClick(picker) {
            const date = new Date()
            date.setTime(date.getTime() + 3600 * 1000 * 24 * 2)
            picker.$emit('pick', date)
          }
        }]
      },

      formInline: {
        start: '',
        end: '',
        time: ''
      },
      locations: [],
      airlinelist: []
    }
  },
  computed: {
    testshow: function() {
      var flag = false
      this.$store.state.user.roles.forEach(function(element) {
        if (element === 'admin') {
          flag = true
        }
      })
      return flag === true
    }
  },
  created() {
    this.getLocations()
    this.fetchAllAirline()
  },
  methods: {
    fetchAllAirline() {
      getAllAirline().then(
        response => {
          this.airlinelist = response.data
        }
      )
    },
    opensuccess(title = '标题', msg = '提示') {
      this.$notify({
        title: title,
        message: msg,
        type: 'success'
      })
    },
    open(title = '标题', msg = '提示') {
      this.$notify({
        title: title,
        message: msg,
        type: 'error'
      })
    },
    // 提交search_flight，根据起始地和时间查询
    onSubmit() {
      if (!this.formInline.start) {
        this.open('error', '请输入起始地')
        return
      }
      if (!this.formInline.end) {
        this.open('error', '请输入目的地')
        return
      }
      if (!this.formInline.time) {
        this.open('error', '请输入时间')
        return
      }
      searchFlight({
        start: this.formInline.start,
        end: this.formInline.end,
        time: this.formInline.time
      }).then(response => {
        if (response.data.msg != null) {
          this.open('error', response.data.msg)
        } else {
          this.loading = false
          this.list = response.data
        }
      })
    },
    getLocations() {
      getAllLocation(getToken()).then(res => {
        res.data.data.forEach((item, index) => {
          this.locations.push({
            id: item.id,
            name: item.name
          })
        })
      })
    },
    // 根据航班号查询
    SubmitByFlightNumber() {
      searchByFlightNumber(this.flightNumber).then(
        response => {
          if (response.data.msg != null) {
            this.open('error', response.data.msg)
          } else {
            this.loading = false
            this.list = response.data
          }
        }
      )
    },
    // 提醒确认购买
    buyFlight(id, ticket) {
      console.log(ticket)
      console.log(id)
      this.$confirm('您将购买该机票, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        console.log(ticket)
        if (ticket > 0) {
          buypost(id).then(res => {
            if (res.data.msg === 'success') {
              this.$message({
                type: 'success',
                message: '购买成功!'
              })
            }
          })
        } else {
          this.buyWait(id)
        }
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消购买'
        })
      })
    },
    buyWait(id) {
      this.$confirm('由于余票数目为0,您将购买候补机票, 当有乘客退票时，将自动为您购买，是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        buywaitpost(id).then(res => {
          if (res.data.msg === 'success') {
            this.$message({
              type: 'success',
              message: '购买成功!'
            })
          } else {
            this.open('error', res.data.msg)
          }
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消购买'
        })
      })
    },
    FlightSort(tabel) {
      flightorder(this.list, tabel.column.order, tabel.prop).then(
        res => {
          this.list = res.data
        }
      )
    },
    // 修改flight
    modityflight(index) {
      this.modformvisable = true
      // 深拷贝
      var objString = JSON.stringify(this.list[index])
      this.flightform = JSON.parse(objString)
    },
    // 提交修改表单
    modifyFlightForm() {
      modifyflightformpost(this.flightform).then(response => {
        if (response.code === 20000) {
          this.opensuccess('success', '更新成功')
        }
      })
      this.modformvisable = false
    },
    deleteFlightForm() {
      deleteflight(this.flightform).then(response => {
        if (response.code === 20000) {
          this.opensuccess('success', '更新成功')
        }
      })
      this.modformvisable = false
    },
    addFlightForm() {
      addflightformpost(this.flightform).then(response => {
        if (response.code === 20000) {
          this.opensuccess('success', '更新成功')
        }
      })
      this.modformvisable = false
    },
    cancelFlight(id, classify) {
      cancelflight(id, classify).then(response => {
        if (response.code === 20000) {
          this.opensuccess('success', '修改成功')
        }
      })
      this.modformvisable = false
    },
    searchFlightLess(classify) {
      if (!this.formInline.start) {
        this.open('error', '请输入起始地')
        return
      }
      if (!this.formInline.end) {
        this.open('error', '请输入目的地')
        return
      }
      if (!this.formInline.time) {
        this.open('error', '请输入时间')
        return
      }
      searchflightless(this.formInline.time, classify, this.formInline.start, this.formInline.end).then(
        res => {
          this.loading = false
          this.list = res.data
        }
      )
    },
    changemethed(tab, event) {
      this.loading = true
      if (tab.label === 'lessprice') {
        this.searchFlightLess('price')
      }
      if (tab.label === 'lesstime') {
        this.searchFlightLess('startTime')
      }
      if (tab.label === 'moreticket') {
        this.searchFlightLess('ticket')
      }
      if (tab.label === 'zonghe') {
        this.searchFlightLess('zonghe')
      }
      if (tab.label === 'direct') {
        this.submit()
      }
      // console.log(tab)
    }
  }
}
</script>

<style scoped>

</style>
